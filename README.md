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
    - [Results on VideoAttentionTarget dataset](#results-videoattentiontarget-dataset)
    - [Results on ChildPlay dataset](#results-childplay-dataset)
  - [Gaze Object Prediction](#gaze-object-prediction)
    - [Results on GOO dataset](#results-goo-dataset)
  - [Human Object Interaction Detection](#human-object-interaction-detection)
    - [Results on HICO-Det dataset](#results-hicodet-dataset)
    - [Results on V-COCO dataset](#results-vcoco-dataset)


## Datasets

### Datasets for Gaze Following Estimation

| Dataset  |  Year  |   Modal     | Dimensions | Data size| Training | Validation | Testing | Evaluation Metric | Annotations | Project |                              
|-----------------------------------------------------|:------:|:------:|:----------------:|:------------:| :------------:|:------------:|:------------:|:------------:| :------------:|:------------:|
|[GazeFollow](https://people.csail.mit.edu/khosla/papers/nips2015_recasens.pdf)|2015|RGB|2D|126,925 |122,143 | - | 4782 | AUC, Min Dist., Avg Dist. | head box, body box, eye location, 2D gaze point, inside/outside| [Project](http://gazefollow.csail.mit.edu/)|
|[VideoGaze](https://openaccess.thecvf.com/content_ICCV_2017/papers/Recasens_Following_Gaze_in_ICCV_2017_paper.pdf)|2017|RGB|2D| 140 movies |120 movies | - | 20 movies| AUC, Min Dist., Dist., KL, AP | head box, outside gaze point| [Project](http://videogazefollow.csail.mit.edu/)|
|[DLGaze](https://arxiv.org/pdf/1907.02364)|2018|RGB|2D| 95,000 |- | - | - | AUC, L2 Dist., Ang. | head box, gaze point| [Project](https://github.com/svip-lab/GazeFollowing)|
|[VideoAttentionTarget](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chong_Detecting_Attended_Visual_Targets_in_Video_CVPR_2020_paper.pdf)|2020|RGB|2D| 50 videos |- | - | - | AUC, L2 Dist., AP | head box, gaze point, inside/outside| [Project](https://github.com/ejcgt/attention-target-detection)|
|[GFIE](https://openaccess.thecvf.com/content/CVPR2023/papers/Hu_GFIE_A_Dataset_and_Baseline_for_Gaze-Following_From_2D_to_CVPR_2023_paper.pdf)|2023|RGB/Depth|2D/3D| 71,799 | 59,217 | 6,281 | 6,281 | AUC, L2 Dist., 3D Dist., 3D Ang. | head box, 2D gaze point, 3D gaze point| [Project](https://sites.google.com/view/gfie)|
|[ChildPlay](hhttps://openaccess.thecvf.com/content/ICCV2023/papers/Tafasca_ChildPlay_A_New_Benchmark_for_Understanding_Childrens_Gaze_Behaviour_ICCV_2023_paper.pdf)|2023|RGB/Depth|2D/3D| 120,549 | -| - | - | AUC, Dist., AP, P.Head | head box, gaze point, gaze class (Is it the head?)| [Project](https://github.com/idiap/geomgaze)|
|[VsGaze](https://openreview.net/pdf?id=ALU676zGFE)|2024|RGB|2D| - | -| - | - | Dist., AP_IO_, F1_LAH, F1_LAEO, AP_SA | head box, gaze point, gaze communication classification label| -|
|[GazeHOI](https://proceedings.neurips.cc/paper_files/paper/2024/file/dbeb7e621d4a554069a6a775da0f7273-Paper-Conference.pdf)|2024|RGB|2D| 43,808 | -| - | - | GazeAcc, Acc@1, Acc@3 | person box, object box, object class and interaction verb| -|


### Datasets for Gaze Object Prediction
| Dataset  |  Year  |   Context     | Data size | Training | Validation | Testing | Evaluation Metric | Annotations | Project |                              
|-----------------------------------------------------|:------:|:------:|:----------------:|:------------:| :------------:|:------------:|:------------:|:------------:| :------------:|
|[GOO-Synth](https://openaccess.thecvf.com/content/CVPR2021W/GAZE/papers/Tomas_GOO_A_Dataset_for_Gaze_Object_Prediction_in_Retail_Environments_CVPRW_2021_paper.pdf) | 2021| Retail| 192,000| -| -| -| AUC, Dist., Ang.,Box AP, Mask AP| head box, eye location, 2D gaze point, object box, gaze object box, segmentation mask| [Project](https://github.com/upeee/GOO-GAZE2021?tab=readme-ov-file) |
|[GOO-Real](https://openaccess.thecvf.com/content/CVPR2021W/GAZE/papers/Tomas_GOO_A_Dataset_for_Gaze_Object_Prediction_in_Retail_Environments_CVPRW_2021_paper.pdf) |2021 |Retail | 9,552| -| -| -| AUC, Dist., Ang.,Box AP | head box, eye location, 2D gaze point, object box, gaze object box | [Project](https://github.com/upeee/GOO-GAZE2021?tab=readme-ov-file) |
|[GESCAM](https://openaccess.thecvf.com/content/CVPR2024W/GAZE/papers/Mathew_GESCAM__A_Dataset_and_Method_on_Gaze_Estimation_for_CVPRW_2024_paper.pdf) |2024 |Classroom | -| -| -| -| AUC, Dist., Ang. | - | [Project](https://athulmmathew.github.io/GESCAM/) |

### Datasets for Human Object Interaction Detection
| Dataset  |  Year | Data size | Training | Validation | Testing | Evaluation Metric  | Project |                              
|-----------------------------------------------------|:------:|:----------------:|:------------:| :------------:|:------------:|:------------:|:------------:|
|[HICO](https://openaccess.thecvf.com/content_iccv_2015/papers/Chao_HICO_A_Benchmark_ICCV_2015_paper.pdf)|2015|47,776 |-|-|-|AP|[Project](http://www.umich.edu/~ywchao/hico/)|
|[HICO-Det](https://arxiv.org/pdf/1702.05448)|2018|47,776 |38,118|-|9,658|Defult AP, Known Object AP|[Project](http://www.umich.edu/~ywchao/hico/)|
|[V-COCO](https://arxiv.org/pdf/1505.04474)|-|10,346 |2,533|2,867|4,946|AP_agent, AP_role|[Project](https://paperswithcode.com/dataset/v-coco)|

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
|[Un-Gaze: A Unified Transformer for Joint Gaze-Location and Gaze-Object Detection](https://ieeexplore.ieee.org/document/10262016)|TCSVT 2023|-|
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
|[Leveraging Multi-Modal Saliency and Fusion for Gaze Target Detection](https://openreview.net/pdf?id=rtdn6GHiLo)|NIPS Gaze Workshop 2023|-|
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
|[Detecting Human-Object Interactions with Action Co-occurrence Priors](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123660715.pdf)|ECCV 2020|[Code](https://github.com/Dong-JinKim/ActionCooccurrencePriors/)|
|[Polysemy Deciphering Network for Human-Object Interaction Detection](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650069.pdf)|ECCV 2020|[Code](https://github.com/MuchHair/PD-Net)|
|[Detailed 2D-3D Joint Representation for Human-Object Interaction](https://openaccess.thecvf.com/content_CVPR_2020/papers/Li_Detailed_2D-3D_Joint_Representation_for_Human-Object_Interaction_CVPR_2020_paper.pdf)|CVPR 2020|[Code](https://github.com/DirtyHarryLYL/DJ-RN)|
|[HOI Analysis: Integrating and Decomposing Human-Object Interaction](https://proceedings.nips.cc/paper_files/paper/2020/file/3493894fa4ea036cfc6433c3e2ee63b0-Paper.pdf)|NIPS 2020|[Code](https://github.com/DirtyHarryLYL/DJ-RN)|
|[Exploiting Scene Graphs for Human-Object Interaction Detection](https://openaccess.thecvf.com/content/ICCV2021/papers/He_Exploiting_Scene_Graphs_for_Human-Object_Interaction_Detection_ICCV_2021_paper.pdf)|ICCV 2021|[Code](https://github.com/ht014/SG2HOI)|
|[Spatially Conditioned Graphs for Detecting Human–Object Interactions](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Spatially_Conditioned_Graphs_for_Detecting_Human-Object_Interactions_ICCV_2021_paper.pdf)|ICCV 2021|[Code](https://github.com/fredzzhang/spatially-conditioned-graphs)|
|[Affordance Transfer Learning for Human-Object Interaction Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Hou_Affordance_Transfer_Learning_for_Human-Object_Interaction_Detection_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/zhihou7/HOI-CL)|
|[Efficient Two-Stage Detection of Human–Object Interactions with a Novel Unary–Pairwise Transformer](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_Efficient_Two-Stage_Detection_of_Human-Object_Interactions_With_a_Novel_Unary-Pairwise_CVPR_2022_paper.pdf)|CVPR 2022|[Code](https://github.com/fredzzhang/upt)/[Project](https://fredzzhang.com/unary-pairwise-transformers/)|


#### One Stage Methods

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[UnionDet: Union-Level Detector Towards Real-Time Human-Object Interaction Detection](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123600494.pdf)|ECCV 2020|-|
|[Learning Human-Object Interaction Detection using Interaction Points](https://openaccess.thecvf.com/content_CVPR_2020/papers/Wang_Learning_Human-Object_Interaction_Detection_Using_Interaction_Points_CVPR_2020_paper.pdf)|CVPR 2020|[Code](https://github.com/vaesl/IP-Net)|
|[PPDM: Parallel Point Detection and Matching for Real-time Human-Object Interaction Detection](https://openaccess.thecvf.com/content_CVPR_2020/papers/Liao_PPDM_Parallel_Point_Detection_and_Matching_for_Real-Time_Human-Object_Interaction_CVPR_2020_paper.pdf)|CVPR 2020|[Code](https://github.com/YueLiao/PPDM)|
|[PPDM: Parallel Point Detection and Matching for Real-time Human-Object Interaction Detection](https://ieeexplore.ieee.org/document/9552553)|TIP 2021|-|
|[End-to-End Human Object Interaction Detection with HOI Transformer](https://openaccess.thecvf.com/content/CVPR2021/papers/Zou_End-to-End_Human_Object_Interaction_Detection_With_HOI_Transformer_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/bbepoch/HoiTransformer)|
|[HOTR: End-to-End Human-Object Interaction Detection with Transformers](https://openaccess.thecvf.com/content/CVPR2021/papers/Kim_HOTR_End-to-End_Human-Object_Interaction_Detection_With_Transformers_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/kakaobrain/hotr)|
|[Glance and Gaze: Inferring Action-aware Points for One-Stage Human-Object Interaction Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Zhong_Glance_and_Gaze_Inferring_Action-Aware_Points_for_One-Stage_Human-Object_Interaction_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/SherlockHolmes221/GGNet)|
|[Visual Relationship Detection Using Part-and-Sum Transformers with Composite Queries](https://openaccess.thecvf.com/content/ICCV2021/papers/Dong_Visual_Relationship_Detection_Using_Part-and-Sum_Transformers_With_Composite_Queries_ICCV_2021_paper.pdf)|ICCV 2021|-|
|[Reformulating HOI Detection as Adaptive Set Prediction](https://openaccess.thecvf.com/content/CVPR2021/papers/Chen_Reformulating_HOI_Detection_As_Adaptive_Set_Prediction_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/yoyomimi/AS-Net)|
|[QPIC: Query-Based Pairwise Human-Object Interaction Detection with Image-Wide Contextual Information](https://openaccess.thecvf.com/content/CVPR2021/papers/Tamura_QPIC_Query-Based_Pairwise_Human-Object_Interaction_Detection_With_Image-Wide_Contextual_Information_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/hitachi-rd-cv/qpic)|
|[Mining the Benefits of Two-stage and One-stage HOI Detection](https://proceedings.neurips.cc/paper/2021/file/8f1d43620bc6bb580df6e80b0dc05c48-Paper.pdf)|NIPS 2021|[Code](https://github.com/YueLiao/CDN)|
|[MSTR: Multi-Scale Transformer for End-to-End Human-Object Interaction Detection](https://openaccess.thecvf.com/content/CVPR2022/papers/Kim_MSTR_Multi-Scale_Transformer_for_End-to-End_Human-Object_Interaction_Detection_CVPR_2022_paper.pdf)|CVPR 2022|-|
|[Human-Object Interaction Detection via Disentangled Transformer](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhou_Human-Object_Interaction_Detection_via_Disentangled_Transformer_CVPR_2022_paper.pdf)|CVPR 2022|-|
|[Iwin: Human-Object Interaction Detection via Transformer with Irregular Windows](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136640085.pdf)|ECCV 2022|-|
|[GEN-VLKT: Simplify Association and Enhance Interaction Understanding for HOI Detection](https://openaccess.thecvf.com/content/CVPR2022/papers/Liao_GEN-VLKT_Simplify_Association_and_Enhance_Interaction_Understanding_for_HOI_Detection_CVPR_2022_paper.pdf)|CVPR 2022|[Code](https://github.com/YueLiao/gen-vlkt)|
|[FGAHOI: Fine-Grained Anchors for Human-Object Interaction Detection](https://ieeexplore.ieee.org/document/10315071)|TPAMI 2023|[Code](https://github.com/xiaomabufei/FGAHOI)|
|[Relational Context Learning for Human-Object Interaction Detection](https://openaccess.thecvf.com/content/CVPR2023/papers/Kim_Relational_Context_Learning_for_Human-Object_Interaction_Detection_CVPR_2023_paper.pdf)|CVPR 2023|[Code](https://github.com/OreoChocolate/MUREN)/[Project](http://cvlab.postech.ac.kr/research/MUREN/)|
|[HOICLIP: Efficient Knowledge Transfer for HOI Detection with Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2023/papers/Ning_HOICLIP_Efficient_Knowledge_Transfer_for_HOI_Detection_With_Vision-Language_Models_CVPR_2023_paper.pdf)|CVPR 2023|[Code](https://github.com/Artanic30/HOICLIP)|
|[Point-Based Learnable Query Generator for Human–Object Interaction Detection](https://ieeexplore.ieee.org/document/10328553)|TIP 2023|-|
|[Toward a Unified Transformer-Based Framework for Scene Graph Generation and Human-Object Interaction Detection](https://ieeexplore.ieee.org/document/10315051)|TIP 2023|-|
|[Exploring Predicate Visual Context in Detecting of Human–Object Interactions](https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_Exploring_Predicate_Visual_Context_in_Detecting_of_Human-Object_Interactions_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/fredzzhang/pvic)|
|[RLIPv2: Fast Scaling of Relational Language-Image Pre-training](https://openaccess.thecvf.com/content/ICCV2023/papers/Yuan_RLIPv2_Fast_Scaling_of_Relational_Language-Image_Pre-Training_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/JacobYuan7/RLIPv2)|
|[Category Query Learning for Human-Object Interaction Classification](https://openaccess.thecvf.com/content/CVPR2023/papers/Xie_Category_Query_Learning_for_Human-Object_Interaction_Classification_CVPR_2023_paper.pdf)|CVPR 2023|[Code](https://github.com/charles-xie/CQL)|
|[ViPLO: Vision Transformer based Pose-Conditioned Self-Loop Graph for Human-Object Interaction Detection](https://openaccess.thecvf.com/content/CVPR2023/papers/Park_ViPLO_Vision_Transformer_Based_Pose-Conditioned_Self-Loop_Graph_for_Human-Object_Interaction_CVPR_2023_paper.pdf)|CVPR 2023|[Code](https://github.com/Jeeseung-Park/ViPLO)|
|[Agglomerative Transformer for Human-Object Interaction Detection](https://openaccess.thecvf.com/content/ICCV2023/papers/Tu_Agglomerative_Transformer_for_Human-Object_Interaction_Detection_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/six6607/AGER)|
|[Re-mine, Learn and Reason: Exploring the Cross-modal Semantic Correlations for Language-guided HOI detection](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Re-mine_Learn_and_Reason_Exploring_the_Cross-modal_Semantic_Correlations_for_ICCV_2023_paper.pdf)|ICCV 2023|-|
|[Re-mine, Learn and Reason: Exploring the Cross-modal Semantic Correlations for Language-guided HOI detection](https://openaccess.thecvf.com/content/ICCV2023/papers/Lei_Efficient_Adaptive_Human-Object_Interaction_Detection_with_Concept-guided_Memory_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/ltttpku/ADA-CM)|
|[TED-Net: Dispersal Attention for Perceiving Interaction Region in Indirectly-Contact HOI Detection](https://ieeexplore.ieee.org/document/10415065)|TCSVT 2024|[Code](https://drliuqi.github.io/)|
|[Disentangled Pre-training for Human-Object Interaction Detection](https://openaccess.thecvf.com/content/CVPR2024/papers/Li_Disentangled_Pre-training_for_Human-Object_Interaction_Detection_CVPR_2024_paper.pdf)|CVPR 2024|[Code](https://github.com/xingaoli/DP-HOI)|
|[Human-Object Interaction Detection Collaborated with Large Relation-driven Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a54def490213ee10631b991c5acc6b5-Paper-Conference.pdf)|NIPS 2024|[Code](https://github.com/0liliulei/DiffusionHOI)|
|[Orchestrating the Symphony of Prompt Distribution Learning for Human-Object Interaction Detection](https://ojs.aaai.org/index.php/AAAI/article/view/32412/34567)|AAAI 2025|-|

## Performance
### Gaze Following Estimation
#### Results on GazeFollow dataset

##### Modality:
I: RGB Image; D: Depth; T: Temporal; O: Object; P: Posture; E: Eye

| Method|  Published in | Backbone(Scene/Head)| CNN/Transformer|Modality|Multi-Person |AUC | Min Dist. | Avg Dist.| Ang.| Param.|                               
|-------------|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|:------------:|
|[GazeFollow](https://people.csail.mit.edu/khosla/papers/nips2015_recasens.pdf)|NIPS 2015|Alexnet/Alexnet|CNN|I|✘|0.878|0.113|0.190|24.0|50M*|
|[Chong-2018](https://openaccess.thecvf.com/content_ECCV_2018/papers/Eunji_Chong_Connecting_Gaze_Scene_ECCV_2018_paper.pdf)|ECCV 2018|ResNet-50/ResNet-50|CNN|I|✘|0.896|0.112|0.187|-|51M*|
|[Lian](https://arxiv.org/pdf/1907.02364)|ACCV 2018|ResNet-50/ResNet-50|CNN|I|✘|0.906|0.081|0.145|17.6|55M|
|[Chong-2020](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chong_Detecting_Attended_Visual_Targets_in_Video_CVPR_2020_paper.pdf)|CVPR 2020|ResNet-50/ResNet-50|CNN|I+T|✘|0.921|0.077|0.137|-|61M|
|[Fang](https://openaccess.thecvf.com/content/CVPR2021/papers/Fang_Dual_Attention_Guided_Gaze_Target_Detection_in_the_Wild_CVPR_2021_paper.pdf)|CVPR 2021|ResNet-50/ResNet-34|CNN|I+D+E|✘|0.922|0.067|0.124|14.9|68M|
|[Jin](https://ieeexplore.ieee.org/document/9666980)|FG 2021|ResNet-50/ResNet-50|CNN|I|✘|0.919|0.076|0.126|-|-|
|[Jin*](https://ieeexplore.ieee.org/document/9666980)|FG 2021|GhostNet/GhostNet|CNN|I|✘|0.918|0.082|0.132|-|-|
|[ESCNet](https://openaccess.thecvf.com/content/CVPR2022/papers/Bao_ESCNet_Gaze_Target_Detection_With_the_Understanding_of_3D_Scenes_CVPR_2022_paper.pdf)|CVPR 2022|ResNet-50/ResNet-50|CNN|I+D+P|✘|0.928|-|0.126|15.3| 29M*|
|[ESCNet-3D](https://openaccess.thecvf.com/content/CVPR2022/papers/Bao_ESCNet_Gaze_Target_Detection_With_the_Understanding_of_3D_Scenes_CVPR_2022_paper.pdf)|CVPR 2022|ResNet-50/ResNet-50|CNN|I+D+P|✘|0.928|-|0.122|14.6| 29M*|
|[TPNet](https://ieeexplore.ieee.org/document/9398702)|TCSVT 2022|Alexnet/Alexnet||I+O||0.908|0.074|0.136|16.5| 50M*|
|[Hu](https://ieeexplore.ieee.org/document/9740573)|TIM 2022|ResNet-50/ResNet-50|CNN|I|✘|-|0.075|0.135|-| -|
|[HGTTR](https://arxiv.org/pdf/2203.10433)|CVPR 2022|ResNet-50/-|Transformer|I|✔ |0.917|0.069|0.133|-| 43M|
|[HGTTR*](https://arxiv.org/pdf/2203.10433)|CVPR 2022|ResNet-50/-|Transformer|I|✔|0.905|0.065|0.138|-| 43M|
|[Gupta](https://openaccess.thecvf.com/content/CVPR2022W/GAZE/papers/Gupta_A_Modular_Multimodal_Architecture_for_Gaze_Target_Prediction_Application_to_CVPRW_2022_paper.pdf)|CVPRW 2022|ResNet-50/ResNet-50|CNN|I+D+P|✘|0.943|0.056|0.114|-| 35M|
|[Jin](https://www.sciencedirect.com/science/article/pii/S0952197622001464)|EAAI 2022|ResNet-50/ResNet-50|CNN|I+D+P|✘|0.923|0.064|0.120|14.8| >52M*|
|[Jin*](https://www.sciencedirect.com/science/article/pii/S0952197622001464)|EAAI 2022|Res2Net-50/Res2Net-50|CNN|I+D+P|✘|0.920|0.063|0.118|14.8| >52M*|
|[TONINI](https://dl.acm.org/doi/10.1145/3536221.3556624)|ICMI 2022|ResNet-50/ResNet-50|CNN|I|✘|0.927|-|0.141|-| 92M|
|[VSG-IA](https://ieeexplore.ieee.org/document/9828503)|TCSVT 2022|ResNet-50/ResNet-50|CNN/Transformer|I+D+O|✘|0.923|0.069|0.128|-| -|
|[Miao](https://openaccess.thecvf.com/content/WACV2023/papers/Miao_Patch-Level_Gaze_Distribution_Prediction_for_Gaze_Following_WACV_2023_paper.pdf)|WACV 2023|ResNet-50/ResNet-50|CNN|I+D+T|✘|0.928|0.072|0.131|-| 61M|
|[Miao*](https://openaccess.thecvf.com/content/WACV2023/papers/Miao_Patch-Level_Gaze_Distribution_Prediction_for_Gaze_Following_WACV_2023_paper.pdf)|WACV 2023|ResNet-50/ResNet-50|CNN|I+D|✘|0.934|0.065|0.123|-| 61M|
|[GFIE](https://openaccess.thecvf.com/content/CVPR2023/papers/Hu_GFIE_A_Dataset_and_Baseline_for_Gaze-Following_From_2D_to_CVPR_2023_paper.pdf)|CVPR 2023|ResNet-50/ResNet-50|CNN|I+D|✘|-|-|-|-| -|
|[ChildPlay](https://openaccess.thecvf.com/content/ICCV2023/papers/Tafasca_ChildPlay_A_New_Benchmark_for_Understanding_Childrens_Gaze_Behaviour_ICCV_2023_paper.pdf)|ICCV 2023|ResNet-50/ResNet-18|CNN|I|✘|0.939|0.062|0.122|-| >25M*|
|[ChildPlay-3D](https://openaccess.thecvf.com/content/ICCV2023/papers/Tafasca_ChildPlay_A_New_Benchmark_for_Understanding_Childrens_Gaze_Behaviour_ICCV_2023_paper.pdf)|ICCV 2023|ResNet-50/ResNet-18|CNN|I|✘|0.936|0.064|0.124|-| >25M*|
|[Tonini](https://openaccess.thecvf.com/content/ICCV2023/papers/Tonini_Object-aware_Gaze_Target_Detection_ICCV_2023_paper.pdf)|ICCV 2023|ResNet-50|Transformer|I+O||0.922|0.033|0.069|-| 54M|
|[Tonini](https://openaccess.thecvf.com/content/ICCV2023/papers/Tonini_Object-aware_Gaze_Target_Detection_ICCV_2023_paper.pdf)|ICCV 2023|ResNet-50|Transformer|I+D+O|✔|0.922|0.029|0.072|-| 54M|
|[MMSF](https://openreview.net/pdf?id=rtdn6GHiLo)|NIPS Gaze Workshop 2023|ResNet-50/ResNet-50|CNN|I+D|✔|0.932|0.073|0.133|-| -|
|[Un-Gaze](https://openreview.net/pdf?id=rtdn6GHiLo)|TCSVT 2023|ResNet-50|Transformer|I|✔|0.928|0.057|0.114|-| -|
|[Un-Gaze](https://openreview.net/pdf?id=rtdn6GHiLo)|TCSVT 2023|ResNet-101|Transformer|I|✔|0.925|0.064|0.116|-| -|
|[Yang](https://eccv.ecva.net/virtual/2024/poster/1131)|ECCV 2024|ResNet-50/ResNet-50|CNN|I|✘|0.939|0.059|0.114|12.4|-|
|[Yang](https://ojs.aaai.org/index.php/AAAI/article/view/28480)|AAAI 2024|ResNet-50/ResNet-50|CNN|I+O+P|✘|-|0.061|0.118|-|-|
|[Depth Matters](https://dl.acm.org/doi/10.1145/3689643)|TOMM 2024|ResNet-50/ResNet-50|CNN|I|✘|0.927|0.075|0.132|16.7|-|
|[Depth Matters](https://dl.acm.org/doi/10.1145/3689643)|TOMM 2024|ResNet-50/ResNet-50|CNN|I+D|✘|0.936|0.061|0.121|14.5|-|
|[Gupta](https://publications.idiap.ch/attachments/papers/2024/Gupta_FG_2024.pdf)|FG 2024|ViT/ResNet-18|CNN/Transformer|I|✔|-|-|-|-|-|
|[Gupta](https://openreview.net/pdf?id=ALU676zGFE)|NIPS 2024|ViT/ResNet-18|CNN/Transformer|I|✔|0.929|0.062|0.118|-|-|
|[ViTGaze](https://link.springer.com/article/10.1007/s44267-024-00064-9)|Visual Intelligence 2024|ViT-S|Transformer|I|✘|0.949|0.047|0.105|-|22M|
|[Sharingan](https://openaccess.thecvf.com/content/CVPR2024/papers/Tafasca_Sharingan_A_Transformer_Architecture_for_Multi-Person_Gaze_Following_CVPR_2024_paper.pdf)|CVPR 2024|ViT/ResNet-18|Transformer|I|✔|0.944|0.057|0.113|-|>135M*|
|[Tafasca](https://openreview.net/pdf?id=BAmAFraxvf)|NIPS 2024|ViT/ResNet-18|Transformer|I|✔|-|0.051|0.108|-|-|
|[GazeLLE](https://arxiv.org/pdf/2412.09586)|CVPR 2025|ViT-B|Transformer|I|✔|0.956|0.045|0.104|-|86M+2.8M|
|[GazeLLE](https://arxiv.org/pdf/2412.09586)|CVPR 2025|ViT-L|Transformer|I|✔|0.958|0.041|0.099|-|307M+2.8M|


