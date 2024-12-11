# EEG Data Curation & BIDS Conversion

To facilitate data handling and preprocessing, we employ [EEG2BIDS Wizard](https://github.com/aces/eeg2bids), a custom MATLAB application installed at all HBCD sites. After each EEG session, raw data are uploaded to the Wizard, which, among other things, converts this data to the BIDS standard data structure. The resulting BIDS data structure is:
```
assembly_bids/ 
|__ participants.tsv
|__ participants.json 
|__ sub-<label>/
|   |__ sub-<label>_sessions.tsv
|   |__ sub-<label>_sessions.json
|   |__ ses-<label>/
|       |__ eeg/
|       |

(Location of electrodes)
|       |   |__sub-<label>_ses-<label>_acq-ecg_space-CapTrak_electrodes.tsv
|       |   |__sub-<label>_ses-<label>_acq-ecg_space-CapTrak_coordsystem.json
|       |   |__sub-<label>_ses-<label>_acq-eeg_space-<CapTrak/CTF>_electrodes.tsv
|       |   |__sub-<label>_ses-<label>_acq-eeg_space-<CapTrak/CTF>_coordsystem.json

(Task acquisitions)
|       |   |__sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-<eeg/ecg>_channels.tsv
|       |   |__sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-<eeg/ecg>_eeg.json
|       |   |__sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-<eeg/ecg>_eeg.set
|       |   |__sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-<eeg/ecg>_events.tsv
|       |   |__sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-<eeg/ecg>_events.json
|       |   |
|       |   |__ sourcedata/
|       |       |__ sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-eeg_flags.json
|       |       |__ sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-eeg_impedances.json
|       |       |__ sub-<label>_ses-<label>_task-<FACE/MMN/RS/VEP>_acq-eeg_eventlogs.txt
```

The specific **location of electrodes**, placed on either the head (`acq-eeg`) or chest (`acq-ecg`), is specified in the `*_electrodes.tsv` files following cartesian coordinates provided by the accompanying `*_coordsystem.json` file. For **task acquisitions**, the task is specified by `task-<label>`, with task options of `FACE`, `MMN`, `RS`, and `VEP` (see task details [here](../measures/eeg/overview.md#eeg-parameters)).

<ul>
The accompanying <code>sourcedata/</code> files include:
<li>Information about quality control flags and acquisition (<code>*_flags.json</code>- see QC details <a href="../../measures/eeg/overview#quality-control-known-issues">here</a>)</li>
<li>Impedance values used to ensure good electrode contact (<code>*_impedence.json</code>)</li>
<li>Task stimuli presentations (<code>*_eventlogs.txt</code>)</li>
</ul>