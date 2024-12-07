# Processing Pipelines & Documentation

<p style="font-size: 1.2em; margin: 40px 0 0; font-weight: normal; padding-bottom: 5px; border-bottom: none;">
<i>For full documentation on how each pipeline was used for HBCD processing, please visit the external <a href="https://hbcd-cbrain-processing.readthedocs.io/latest/">HBCD Processing</a> page</i>. The following pipelines were used for HBCD data processing:</p> 

### Magnetic Resonance Imaging (MRI)
<ul style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
  <li style="margin-bottom: 10px;">
    <a href="https://mriqc.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      MRIQC
    </a>: automated extraction of image quality metrics from structural and functional MRI data
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://bibsnet.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      BIBSNet
    </a>: deep learning model for brain segmentation
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://nibabies.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      infant-fMRIPrep
    </a>: structural and functional MRI preprocessing pipeline
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://xcp-d.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      XCP-D
    </a>: functional MRI post-processing and noise regression pipeline
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://qsiprep.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      QSIPrep
    </a> and 
    <a href="https://qsirecon.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      QSIRecon
    </a>: diffusion-weighted MRI (dMRI) data processing pipelines
  </li>
  <li style="margin-bottom: 10px;">
    <a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      qMRI Postproc 
    </a>: minimal post-processing for SyMRI synthetic images derived from QALAS acquisition
  </li>
</ul>

### Electroencephalogram (EEG)
<p style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
    <a href="https://docs-hbcd-made.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      HBCD-MADE
    </a>: Maryland Analysis of Developmental EEG (MADE) pipeline adapted for HBCD
</p>

### Magnetic Resonance Spectroscopy (MRS)       
<p style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
    <a href="https://osprey-bids.readthedocs.io/en/latest/index.html" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      OSPREY-BIDS
    </a>: MRS data processing pipeline
</p>

### Biosensor Data      
<p style="list-style-type: none; padding: 0; font-family: Arial, sans-serif;">
    <a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/" style="color: #2a7ae2; text-decoration: none; font-weight: bold;">
      HBCD-Motion
    </a>: leg movement sensor data processing
</p>
