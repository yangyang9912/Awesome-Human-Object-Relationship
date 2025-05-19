## Awesome Human-Object Relationship Understanding [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


## Menu
- [Datasets](#datasets)
  - [Datasets for Gaze Following Estimation](#datasets-for-gaze-following-estimation)
  - [Datasets for Gaze Object Prediction](#datasets-for-gaze-object-prediction)
  - [Datasets for Human Object Interaction Detection](#datasets-for-human-object-interaction-detection)
- [Human-Object Relationship Understanding Methods](#methods)
  - [Methods for Gaze Following Estimation](#methods-for-gaze-following-estimation)
    - [Single Modal Methods](#single-modal)
    - [Multi Modal Methods](#multi-modal)
  - [Methods for Gaze Object Prediction](#methods-for-gaze-object-prediction)
  - [Methods for Human Object Interaction Detection](#methods-for-human-object-interaction-detection)
    - [Two Stage Methods](#two-stage)
    - [One Stage Methods](#one-stage)
- [Performance](#performance)
  - [Gaze Following Estimation](#gaze-following-estimation)
    - [Results on GazeFollow dataset](#results-gazefollow-dataset)
    - [Results on VideoAttentionTarget dataset](#gresults-videoattentiontarget-dataset)
  - [Gaze Object Prediction](#gaze-object-prediction)
    - [Results on GOO dataset](#results-goo-dataset)
  - [Human Object Interaction Detection](#human-object-interaction-detection)
    - [Results on HICO-Det dataset](#results-hicodet-dataset)
    - [Results on V-COCO dataset](#results-vcoco-dataset)


## Datasets

### Datasets for Gaze Following Estimation


### Datasets for Gaze Object Prediction


### Datasets for Human Object Interaction Detection



## Human-Object Relationship Understanding Methods



### Methods for Gaze Following Estimation

#### Single Modal Methods

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[Where are They Looking?](https://people.csail.mit.edu/khosla/papers/nips2015_recasens.pdf)|NIPS 2015|[Project](http://gazefollow.csail.mit.edu/)|
|[Connecting Gaze, Scene, and Attention: Generalized Attention Estimation via Joint Modeling of Gaze and Scene Saliency](https://openaccess.thecvf.com/content_ECCV_2018/papers/Eunji_Chong_Connecting_Gaze_Scene_ECCV_2018_paper.pdf)|ECCV 2018|-|
|[Believe It or Not, We Know What You Are Looking at!](https://arxiv.org/pdf/1907.02364)|ACCV 2018|[Code](https://github.com/svip-lab/GazeFollowing)|
|[Detecting Attended Visual Targets in Video](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chong_Detecting_Attended_Visual_Targets_in_Video_CVPR_2020_paper.pdf)|CVPR 2020|[Code](https://github.com/ejcgt/attention-target-detection)|
|[Multi-Person Gaze-Following with Numerical Coordinate Regression](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9666980)|FG 2021|[Code](https://github.com/moshuilanting/multi-person-gaze-following)|
|[End-to-End Human-Gaze-Target Detection with Transformers](https://openaccess.thecvf.com/content/CVPR2022/papers/Tu_End-to-End_Human-Gaze-Target_Detection_With_Transformers_CVPR_2022_paper.pdf)|CVPR 2022|-|
|[Un-Gaze: A Unified Transformer for Joint Gaze-Location and Gaze-Object Detection](https://openreview.net/pdf?id=rtdn6GHiLo)|NIPS Gaze Workshop 2023|-|
|[Sharingan: A Transformer Architecture for Multi-Person Gaze Following](https://openaccess.thecvf.com/content/CVPR2024/papers/Tafasca_Sharingan_A_Transformer_Architecture_for_Multi-Person_Gaze_Following_CVPR_2024_paper.pdf)|CVPR 2024|[Code](https://github.com/idiap/sharingan)|
|[Gaze Target Detection Based on Head-Local-Global Coordination](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03933.pdf)|ECCV 2024|-|
|[GazeHTA: End-to-end Gaze Target Detection with Head-Target Association](https://arxiv.org/pdf/2404.10718)|Arxiv 2024|-|
|[A Unified Model for Gaze Following and Social Gaze Prediction](https://ieeexplore.ieee.org/document/10581955)|FG 2024|-|
|[A Novel Framework for Multi-Person Temporal Gaze Following and Social Gaze Prediction](https://openreview.net/pdf?id=ALU676zGFE)|NIPS 2024|-|
|[ViTGaze: Gaze Following with Interaction Features in Vision Transformers](https://link.springer.com/article/10.1007/s44267-024-00064-9)|Visual Intelligence 2024|[Code](https://github.com/hustvl/ViTGaze)|
|[Gaze-LLE: Gaze Target Estimation via Large-Scale Learned Encoders](https://arxiv.org/pdf/2412.09586)|CVPR 2025|[Code](https://github.com/fkryan/gazelle)|


#### Multi Modal Methods

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[Dual Attention Guided Gaze Target Detection in the Wild](https://openaccess.thecvf.com/content/CVPR2021/papers/Fang_Dual_Attention_Guided_Gaze_Target_Detection_in_the_Wild_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/Crystal2333/DAM)|
|[ESCNet: Gaze Target Detection with the Understanding of 3D Scenes](https://openaccess.thecvf.com/content/CVPR2022/papers/Bao_ESCNet_Gaze_Target_Detection_With_the_Understanding_of_3D_Scenes_CVPR_2022_paper.pdf)|CVPR 2022|-|
|[Multimodal Across Domains Gaze Target Detection](https://arxiv.org/pdf/2208.10822)|ICMI 2022|[Code](https://github.com/francescotonini/multimodal-across-domains-gaze-target-detection)|
|[Gaze Estimation via the Joint Modeling of Multiple Cues](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9398702)|TCSVT 2022|-|
|[We Know Where They Are Looking at From the RGB-D Camera: Gaze Following in 3D](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9740573)|TCSVT 2022|[Project](https://sites.google.com/view/3dgazefollow)|
|[Gaze Target Estimation Inspired by Interactive Attention](https://ieeexplore.ieee.org/document/9828503)|TCSVT 2022|[Code](https://github.com/nkuhzx/VSG-IA)|
|[A Modular Multimodal Architecture for Gaze Target Prediction](https://openaccess.thecvf.com/content/CVPR2022W/GAZE/papers/Gupta_A_Modular_Multimodal_Architecture_for_Gaze_Target_Prediction_Application_to_CVPRW_2022_paper.pdf)|CVPRW 2022|[Code](https://github.com/idiap/multimodal_gaze_target_prediction)|
|[Depth-aware Gaze Following via Auxiliary Networks for Robotics](https://www.sciencedirect.com/science/article/pii/S0952197622001464)|EAAI 2022|-|
|[Patch-level Gaze Distribution Prediction for Gaze Following](https://openaccess.thecvf.com/content/WACV2023/papers/Miao_Patch-Level_Gaze_Distribution_Prediction_for_Gaze_Following_WACV_2023_paper.pdf)|WACV 2023|[Code](https://github.com/recasens/Gaze-Following)|
|[Patch-level Gaze Distribution Prediction for Gaze Following](https://openaccess.thecvf.com/content/WACV2023/papers/Miao_Patch-Level_Gaze_Distribution_Prediction_for_Gaze_Following_WACV_2023_paper.pdf)|WACV 2023|[Code](https://github.com/qiaomu-miao/gazefollowing_pdp)|
|[ChildPlay: A New Benchmark for Understanding Children’s Gaze Behaviour](https://openaccess.thecvf.com/content/ICCV2023/papers/Tafasca_ChildPlay_A_New_Benchmark_for_Understanding_Childrens_Gaze_Behaviour_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/idiap/geomgaze)|
|[GFIE: A Dataset and Baseline for Gaze-Following from 2D to 3D in Indoor Environments](https://openaccess.thecvf.com/content/CVPR2023/papers/Hu_GFIE_A_Dataset_and_Baseline_for_Gaze-Following_From_2D_to_CVPR_2023_paper.pdf)|ICCV 2023|[Project](https://sites.google.com/view/gfie)|
|[Object-aware Gaze Target Detection](https://openaccess.thecvf.com/content/ICCV2023/papers/Tonini_Object-aware_Gaze_Target_Detection_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/francescotonini/object-aware-gaze-target-detection)|
|[Leveraging Multi-Modal Saliency and Fusion for Gaze Target Detection](https://ieeexplore.ieee.org/document/10262016)|TCSVT 2023|-|
|[Gaze Target Detection by Merging Human Attention and Activity Cues](https://ojs.aaai.org/index.php/AAAI/article/view/28480)|AAAI 2024|-|
|[Depth Matters: Spatial Proximity-based Gaze Cone Generation for Gaze Following in Wild](https://dl.acm.org/doi/10.1145/3689643)|TOMM 2024|[Code](https://github.com/VUT-HFUT/DepthMatters)|
|[Toward Semantic Gaze Target Detection](https://proceedings.neurips.cc/paper_files/paper/2024/file/dbeb7e621d4a554069a6a775da0f7273-Paper-Conference.pdf)|NIPS 2024|-|


### Methods for Gaze Object Prediction

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[GaTector: A Unified Framework for Gaze Object Prediction](https://openaccess.thecvf.com/content/CVPR2022/papers/Wang_GaTector_A_Unified_Framework_for_Gaze_Object_Prediction_CVPR_2022_paper.pdf)|CVPR 2022|[Code](https://github.com/CodeMonsterPHD/GaTector-A-Unified-Framework-for-Gaze-Object-Prediction)|
|[TransGOP: Transformer-Based Gaze Object Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/28883/29678)|AAAI 2024|[Code](https://github.com/chenxi-guo/transgop)|
|[Boosting Gaze Object Prediction via Pixel-level Supervision from Vision Foundation Model](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08783.pdf)|ECCV 2024|[Code](https://github.com/jinyang06/SamGOP)|


### Methods for Human Object Interaction Detection

#### Two Stage Methods

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[Learning to Detect Human-Object Interactions](https://arxiv.org/pdf/1702.05448)|WACV 2018|-|
|[Detecting and Recognizing Human-Object Interactions](https://openaccess.thecvf.com/content_cvpr_2018/papers/Gkioxari_Detecting_and_Recognizing_CVPR_2018_paper.pdf)|CVPR 2018|-|
|[Learning Human-Object Interactions by Graph Parsing Neural Networks](https://openaccess.thecvf.com/content_cvpr_2018/papers/Gkioxari_Detecting_and_Recognizing_CVPR_2018_paper.pdf)|ECCV 2018|[Code](https://github.com/SiyuanQi-zz/gpnn)|
|[iCAN: Instance-Centric Attention Network for Human-Object Interaction Detection](https://arxiv.org/abs/1808.10437)|BMVC 2018|[Code](https://github.com/vt-vl-lab/iCAN)/[Project](http://www.chengao.vision/iCAN/)|
|[Pose-aware Multi-level Feature Network for Human Object Interaction Detection](https://openaccess.thecvf.com/content_ICCV_2019/papers/Wan_Pose-Aware_Multi-Level_Feature_Network_for_Human_Object_Interaction_Detection_ICCV_2019_paper.pdf)|ICCV 2019|[Code](https://github.com/bobwan1995/PMFNet)|
|[No-Frills Human-Object Interaction Detection: Factorization, Layout Encodings, and Training Techniques](https://openaccess.thecvf.com/content_ICCV_2019/papers/Gupta_No-Frills_Human-Object_Interaction_Detection_Factorization_Layout_Encodings_and_Training_Techniques_ICCV_2019_paper.pdf)|ICCV 2019|[Code](https://github.com/BigRedT/no_frills_hoi_det)/[Project](https://tanmaygupta.info/no_frills/)|
|[VSGNet: Spatial Attention Network for Detecting Human Object Interactions Using Graph Convolutions](https://openaccess.thecvf.com/content_CVPR_2020/papers/Ulutan_VSGNet_Spatial_Attention_Network_for_Detecting_Human_Object_Interactions_Using_CVPR_2020_paper.pdf)|CVPR 2020|[Code](https://github.com/ASMIftekhar/VSGNet)|
|[Amplifying Key Cues for Human-Object-Interaction Detection](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123590239.pdf)|ECCV 2020|-|

#### One Stage Methods






