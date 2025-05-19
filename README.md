## Awesome Human-Object Relationship Understanding [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


## Menu
- [Datasets](#datasets)
  - [Datasets for Gaze Following Estimation](#datasets-for-gaze-following-estimation)
  - [Datasets for Gaze Object Prediction](#datasets-for-gaze-object-prediction)
  - [Datasets for Human Object Interaction Detection](#datasets-for-human-object-interaction-detection)
- [Human-Object Relationship Understanding Methods](#methods)
  - [Methods for Gaze Following Estimation](#methods-for-gaze-following-estimation)
  - [Methods for Gaze Object Prediction](#methods-for-gaze-object-prediction)
  - [Methods for Human Object Interaction Detection](#methods-for-human-object-interaction-detection)
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

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[Where are They Looking?](https://people.csail.mit.edu/khosla/papers/nips2015_recasens.pdf)|NIPS 2015|[Project](http://gazefollow.csail.mit.edu/)|
|[Connecting Gaze, Scene, and Attention: Generalized Attention Estimation via Joint Modeling of Gaze and Scene Saliency](https://openaccess.thecvf.com/content_ECCV_2018/papers/Eunji_Chong_Connecting_Gaze_Scene_ECCV_2018_paper.pdf)|ECCV 2018|-|
|[Believe It or Not, We Know What You Are Looking at!](https://arxiv.org/pdf/1907.02364)|ACCV 2018|[Code](https://github.com/svip-lab/GazeFollowing)|
|[Detecting Attended Visual Targets in Video](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chong_Detecting_Attended_Visual_Targets_in_Video_CVPR_2020_paper.pdf)|CVPR 2020|[Code](https://github.com/ejcgt/attention-target-detection)|
|[Dual Attention Guided Gaze Target Detection in the Wild](https://openaccess.thecvf.com/content/CVPR2021/papers/Fang_Dual_Attention_Guided_Gaze_Target_Detection_in_the_Wild_CVPR_2021_paper.pdf)|CVPR 2021|[Code](https://github.com/Crystal2333/DAM)|
|[Multi-Person Gaze-Following with Numerical Coordinate Regression](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9666980)|FG 2021|[Code](https://github.com/moshuilanting/multi-person-gaze-following)|
|[ESCNet: Gaze Target Detection with the Understanding of 3D Scenes](https://openaccess.thecvf.com/content/CVPR2022/papers/Bao_ESCNet_Gaze_Target_Detection_With_the_Understanding_of_3D_Scenes_CVPR_2022_paper.pdf)|CVPR 2022|-|
|[Multimodal Across Domains Gaze Target Detection](https://arxiv.org/pdf/2208.10822)|ICMI 2022|[Code](https://github.com/francescotonini/multimodal-across-domains-gaze-target-detection)|
|[Gaze Estimation via the Joint Modeling of Multiple Cues](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9398702)|TCSVT 2022|-|
|[We Know Where They Are Looking at From the RGB-D Camera: Gaze Following in 3D](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9740573)|TCSVT 2022|[Project](https://sites.google.com/view/3dgazefollow)|
|[Gaze Target Estimation Inspired by Interactive Attention](https://ieeexplore.ieee.org/document/9828503)|TCSVT 2022|[Code](https://github.com/nkuhzx/VSG-IA)|
|[End-to-End Human-Gaze-Target Detection with Transformers](https://openaccess.thecvf.com/content/CVPR2022/papers/Tu_End-to-End_Human-Gaze-Target_Detection_With_Transformers_CVPR_2022_paper.pdf)|CVPR 2022|-|
|[A Modular Multimodal Architecture for Gaze Target Prediction](https://openaccess.thecvf.com/content/CVPR2022W/GAZE/papers/Gupta_A_Modular_Multimodal_Architecture_for_Gaze_Target_Prediction_Application_to_CVPRW_2022_paper.pdf)|CVPRW 2022|[Code](https://github.com/idiap/multimodal_gaze_target_prediction)|
|[Depth-aware Gaze Following via Auxiliary Networks for Robotics](https://www.sciencedirect.com/science/article/pii/S0952197622001464)|EAAI 2022|-|
|[Patch-level Gaze Distribution Prediction for Gaze Following](https://openaccess.thecvf.com/content/WACV2023/papers/Miao_Patch-Level_Gaze_Distribution_Prediction_for_Gaze_Following_WACV_2023_paper.pdf)|WACV 2023|[Code](https://github.com/recasens/Gaze-Following)|
|[Patch-level Gaze Distribution Prediction for Gaze Following](https://openaccess.thecvf.com/content/WACV2023/papers/Miao_Patch-Level_Gaze_Distribution_Prediction_for_Gaze_Following_WACV_2023_paper.pdf)|WACV 2023|[Code](https://github.com/qiaomu-miao/gazefollowing_pdp)|
|[ChildPlay: A New Benchmark for Understanding Children’s Gaze Behaviour](https://openaccess.thecvf.com/content/ICCV2023/papers/Tafasca_ChildPlay_A_New_Benchmark_for_Understanding_Childrens_Gaze_Behaviour_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/idiap/geomgaze)|
|[GFIE: A Dataset and Baseline for Gaze-Following from 2D to 3D in Indoor Environments](https://openaccess.thecvf.com/content/CVPR2023/papers/Hu_GFIE_A_Dataset_and_Baseline_for_Gaze-Following_From_2D_to_CVPR_2023_paper.pdf)|ICCV 2023|[Project](https://sites.google.com/view/gfie)|
|[Object-aware Gaze Target Detection](https://openaccess.thecvf.com/content/ICCV2023/papers/Tonini_Object-aware_Gaze_Target_Detection_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/francescotonini/object-aware-gaze-target-detection)|
|[Leveraging Multi-Modal Saliency and Fusion for Gaze Target Detection](https://ieeexplore.ieee.org/document/10262016)|TCSVT 2023|-|
|[Un-Gaze: A Unified Transformer for Joint Gaze-Location and Gaze-Object Detection](https://openreview.net/pdf?id=rtdn6GHiLo)|NIPS Gaze Workshop 2023|-|
|[Sharingan: A Transformer Architecture for Multi-Person Gaze Following](https://openaccess.thecvf.com/content/CVPR2024/papers/Tafasca_Sharingan_A_Transformer_Architecture_for_Multi-Person_Gaze_Following_CVPR_2024_paper.pdf)|CVPR 2024|[Code](https://github.com/idiap/sharingan)|
|[Gaze Target Detection Based on Head-Local-Global Coordination](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03933.pdf)|ECCV 2024|-|
|[GazeHTA: End-to-end Gaze Target Detection with Head-Target Association](https://arxiv.org/pdf/2404.10718)|Arxiv 2024|-|
|[Gaze Target Detection by Merging Human Attention and Activity Cues](https://ojs.aaai.org/index.php/AAAI/article/view/28480)|AAAI 2024|-|
|[Depth Matters: Spatial Proximity-based Gaze Cone Generation for Gaze Following in Wild](https://dl.acm.org/doi/10.1145/3689643)|TOMM 2024|[Code](https://github.com/VUT-HFUT/DepthMatters)|
|[A Unified Model for Gaze Following and Social Gaze Prediction](https://ieeexplore.ieee.org/document/10581955)|FG 2024|-|
|[A Novel Framework for Multi-Person Temporal Gaze Following and Social Gaze Prediction](https://openreview.net/pdf?id=ALU676zGFE)|NIPS 2024|-|
|[Toward Semantic Gaze Target Detection](https://proceedings.neurips.cc/paper_files/paper/2024/file/dbeb7e621d4a554069a6a775da0f7273-Paper-Conference.pdf)|NIPS 2024|-|
|[ViTGaze: Gaze Following with Interaction Features in Vision Transformers](https://link.springer.com/article/10.1007/s44267-024-00064-9)|Visual Intelligence 2024|[Code](https://github.com/hustvl/ViTGaze)|
|[Gaze-LLE: Gaze Target Estimation via Large-Scale Learned Encoders](https://arxiv.org/pdf/2412.09586)|CVPR 2025|[Code](https://github.com/fkryan/gazelle)|








### Pre-training with Generative Objective

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[FLAVA: A Foundational Language And Vision Alignment Model](https://arxiv.org/abs/2112.04482)|CVPR 2022|[Code](https://github.com/facebookresearch/multimodal/tree/main/examples/flava)|
|[CoCa: Contrastive Captioners are Image-Text Foundation Models](https://arxiv.org/abs/2205.01917)|arXiv 2022|[Code](https://github.com/lucidrains/CoCa-pytorch)|
|[Too Large; Data Reduction for Vision-Language Pre-Training](https://arxiv.org/abs/2305.20087)|arXiv 2023|[Code](https://github.com/showlab/data-centric.vlp)|
|[SAM: Segment Anything](https://arxiv.org/abs/2304.02643)|arXiv 2023|[Code](https://github.com/facebookresearch/segment-anything)|
|[SEEM: Segment Everything Everywhere All at Once](https://arxiv.org/pdf/2304.06718.pdf)|arXiv 2023|[Code](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once)|
|[Semantic-SAM: Segment and Recognize Anything at Any Granularity](https://arxiv.org/pdf/2307.04767.pdf)|arXiv 2023|[Code](https://github.com/UX-Decoder/Semantic-SAM)|
|[Generative Region-Language Pretraining for Open-Ended Object Detection](https://arxiv.org/pdf/2403.10191v1.pdf)|CVPR 2024|[Code](https://github.com/FoundationVision/GenerateU)|
|[InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks](https://arxiv.org/abs/2312.14238)|CVPR 2024|[Code](https://github.com/OpenGVLab/InternVL)|
|[VILA: On Pre-training for Visual Language Models](https://arxiv.org/abs/2312.07533)|CVPR 2024|-|
|[Enhancing Vision-Language Pre-training with Rich Supervisions](https://arxiv.org/pdf/2403.03346v1.pdf)|CVPR 2024|-|
|[Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://arxiv.org/abs/2309.04669)|ICLR 2024|[Code](https://github.com/jy0205/LaVIT)|
|[MMICL: Empowering Vision-language Model with Multi-Modal In-Context Learning](https://arxiv.org/abs/2309.07915)|ICLR 2024|[Code](https://github.com/PKUnlp-icler/MIC)|
|[RLAIF-V: Aligning MLLMs through Open-Source AI Feedback for Super GPT-4V Trustworthiness](https://arxiv.org/abs/2405.17220)|arXiv 2024|[Code](https://github.com/RLHF-V/RLAIF-V)|
|[RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback](https://openaccess.thecvf.com/content/CVPR2024/papers/Yu_RLHF-V_Towards_Trustworthy_MLLMs_via_Behavior_Alignment_from_Fine-grained_Correctional_CVPR_2024_paper.pdf)|CVPR 2024|[Code](https://github.com/RLHF-V/RLHF-V)|
|[Efficient Vision-Language Pre-training by Cluster Masking](https://arxiv.org/pdf/2405.08815)|CVPR 2024|[Code](https://github.com/Zi-hao-Wei/Efficient-Vision-Language-Pre-training-by-Cluster-Masking)|




### Pre-training with Alignment Objective

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[GLIP: Grounded Language-Image Pre-training](https://arxiv.org/abs/2112.03857)|CVPR 2022|[Code](https://github.com/microsoft/GLIP)|
|[DetCLIP: Dictionary-Enriched Visual-Concept Paralleled Pre-training for Open-world Detection](https://arxiv.org/abs/2209.09407)|NeurIPS 2022|-|
|[nCLIP: Non-Contrastive Learning Meets Language-Image Pre-Training](https://arxiv.org/abs/2210.09304)|CVPR 2023|[Code](https://github.com/shallowtoil/xclip)|
|[Do Vision and Language Encoders Represent the World Similarly?](https://openaccess.thecvf.com/content/CVPR2024/papers/Maniparambil_Do_Vision_and_Language_Encoders_Represent_the_World_Similarly_CVPR_2024_paper.pdf)|CVPR 2024|[Code](https://github.com/mayug/0-shot-llm-vision)|
|[Non-autoregressive Sequence-to-Sequence Vision-Language Models](https://arxiv.org/abs/2403.02249v1)|CVPR 2024|-|


## Vision-Language Model Transfer Learning Methods

### Transfer with Prompt Tuning

#### Transfer with Text Prompt Tuning

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[CoOp: Learning to Prompt for Vision-Language Models](https://arxiv.org/abs/2109.01134)|IJCV 2022|[Code](https://github.com/KaiyangZhou/CoOp)|
|[CoCoOp: Conditional Prompt Learning for Vision-Language Models](https://arxiv.org/abs/2203.05557)|CVPR 2022|[Code](https://github.com/KaiyangZhou/CoOp)|
|[ProDA: Prompt Distribution Learning](https://arxiv.org/abs/2205.03340)|CVPR 2022|-|
|[DenseClip: Language-Guided Dense Prediction with Context-Aware Prompting](https://arxiv.org/abs/2112.01518)|CVPR 2022|[Code](https://github.com/raoyongming/DenseCLIP)|
|[TPT: Test-time prompt tuning for zero-shot generalization in vision-language models](https://arxiv.org/abs/2209.07511)|NeurIPS 2022|[Code](https://github.com/azshue/TPT)|
|[DualCoOp: Fast Adaptation to Multi-Label Recognition with Limited Annotations](https://arxiv.org/abs/2206.09541)|NeurIPS 2022|[Code](https://github.com/sunxm2357/DualCoOp)|
|[CPL: Counterfactual Prompt Learning for Vision and Language Models](https://arxiv.org/abs/2210.10362)|EMNLP 2022|[Code](https://github.com/eric-ai-lab/CPL)|
|[Bayesian Prompt Learning for Image-Language Model Generalization](https://arxiv.org/abs/2210.02390v2)|arXiv 2022|-|
|[UPL: Unsupervised Prompt Learning for Vision-Language Models](https://arxiv.org/abs/2204.03649)|arXiv 2022|[Code](https://github.com/tonyhuang2022/UPL)|
|[ProGrad: Prompt-aligned Gradient for Prompt Tuning](https://arxiv.org/abs/2205.14865)|arXiv 2022|[Code](https://github.com/BeierZhu/Prompt-align)|
|[SoftCPT: Prompt Tuning with Soft Context Sharing for Vision-Language Models](https://arxiv.org/abs/2208.13474)|arXiv 2022|[Code](https://github.com/kding1225/softcpt)|
|[SubPT: Understanding and Mitigating Overfitting in Prompt Tuning for Vision-Language Models](https://arxiv.org/abs/2211.02219)|TCSVT 2023|[Code](https://github.com/machengcheng2016/Subspace-Prompt-Learning)|
|[LASP: Text-to-Text Optimization for Language-Aware Soft Prompting of Vision & Language Models](https://arxiv.org/abs/2210.01115)|CVPR 2023|[Code](https://www.adrianbulat.com/lasp)|
|[LMPT: Prompt Tuning with Class-Specific Embedding Loss for Long-tailed Multi-Label Visual Recognition](https://arxiv.org/abs/2305.04536)|ACLW 2024|[Code](https://github.com/richard-peng-xia/LMPT)|
|[Texts as Images in Prompt Tuning for Multi-Label Image Recognition](https://arxiv.org/abs/2211.12739)|CVPR 2023|[code](https://github.com/guozix/TaI-DPT)
|[Visual-Language Prompt Tuning with Knowledge-guided Context Optimization](https://arxiv.org/abs/2303.13283)|CVPR 2023|[Code](https://github.com/htyao89/KgCoOp)|
|[Learning to Name Classes for Vision and Language Models](https://arxiv.org/abs/2304.01830v1)|CVPR 2023|-|
|[PLOT: Prompt Learning with Optimal Transport for Vision-Language Models](https://arxiv.org/abs/2210.01253)|ICLR 2023|[Code](https://github.com/CHENGY12/PLOT)|
|[CuPL: What does a platypus look like? Generating customized prompts for zero-shot image classification](https://arxiv.org/abs/2209.03320)|ICCV 2023|[Code](https://github.com/sarahpratt/CuPL)|
|[ProTeCt: Prompt Tuning for Hierarchical Consistency](https://arxiv.org/abs/2306.02240)|arXiv 2023|-|
|[Enhancing CLIP with CLIP: Exploring Pseudolabeling for Limited-Label Prompt Tuning](https://arxiv.org/abs/2306.01669)|arXiv 2023|[Code](http://github.com/BatsResearch/menghini-enhanceCLIPwithCLIP-code)|
|[Why Is Prompt Tuning for Vision-Language Models Robust to Noisy Labels?](https://arxiv.org/pdf/2307.11978v1.pdf)|ICCV 2023|[Code](https://github.com/CEWu/PTNL)|
|[Gradient-Regulated Meta-Prompt Learning for Generalizable Vision-Language Models](https://arxiv.org/pdf/2303.06571.pdf)|ICCV 2023|-|
|[Knowledge-Aware Prompt Tuning for Generalizable Vision-Language Models](https://arxiv.org/pdf/2308.11186v1.pdf)|ICCV 2023|-|
|[Read-only Prompt Optimization for Vision-Language Few-shot Learning](https://arxiv.org/pdf/2308.14960.pdf)|ICCV 2023|[Code](https://github.com/mlvlab/RPO)|
|[Bayesian Prompt Learning for Image-Language Model Generalization](https://arxiv.org/pdf/2210.02390.pdf)|ICCV 2023|[Code](https://github.com/saic-fi/Bayesian-Prompt-Learning)|
|[Distribution-Aware Prompt Tuning for Vision-Language Models](https://arxiv.org/pdf/2309.03406.pdf)|ICCV 2023|[Code](https://github.com/mlvlab/DAPT)|
|[LPT: Long-Tailed Prompt Tuning For Image Classification](https://arxiv.org/pdf/2210.01033.pdf)|ICCV 2023|[Code](https://github.com/DongSky/LPT)|
|[Diverse Data Augmentation with Diffusions for Effective Test-time Prompt Tuning](https://openaccess.thecvf.com/content/ICCV2023/papers/Feng_Diverse_Data_Augmentation_with_Diffusions_for_Effective_Test-time_Prompt_Tuning_ICCV_2023_paper.pdf)|ICCV 2023|[Code](https://github.com/chunmeifeng/DiffTPT)|
|[Efficient Test-Time Prompt Tuning for Vision-Language Models](https://arxiv.org/abs/2408.05775)|arXiv 2024|-|
|[Text-driven Prompt Generation for Vision-Language Models in Federated Learning](https://arxiv.org/abs/2310.06123)|ICLR 2024|-|
|[C-TPT: Calibrated Test-Time Prompt Tuning for Vision-Language Models via Text Feature Dispersion](https://openreview.net/pdf?id=jzzEHTBFOT)|ICLR 2024|-|
|[Prompt Gradient Projection for Continual Learning](https://openreview.net/pdf?id=EH2O3h7sBI)|ICLR 2024|-|
|[Nemesis: Normalizing the soft-prompt vectors of vision-language models](https://openreview.net/pdf?id=zmJDzPh1Dm)|ICLR 2024|[Code](https://github.com/ShyFoo/Nemesis)|
|[DePT: Decomposed Prompt Tuning for Parameter-Efficient Fine-tuning](https://arxiv.org/abs/2309.05173)|ICLR 2024|[Code](https://github.com/ZhengxiangShi/DePT)|
|[TCP:Textual-based Class-aware Prompt tuning for Visual-Language Model](https://arxiv.org/abs/2311.18231)|CVPR 2024|[Code](https://github.com/htyao89/Textual-based_Class-aware_prompt_tuning/)|
|[One Prompt Word is Enough to Boost Adversarial Robustness for Pre-trained Vision-Language Models](https://arxiv.org/abs/2403.01849v1)|CVPR 2024|[Code](https://github.com/TreeLLi/APT)|
|[Any-Shift Prompting for Generalization over Distributions](https://arxiv.org/abs/2402.10099)|CVPR 2024|-|
|[Towards Better Vision-Inspired Vision-Language Models](https://www.lamda.nju.edu.cn/caoyh/files/VIVL.pdf)|CVPR 2024|-|
|[Mind the Interference: Retaining Pre-trained Knowledge in Parameter Efficient Continual Learning of Vision-Language Models](https://arxiv.org/pdf/2407.05342v1)|ECCV 2024|[Code](https://github.com/lloongx/DIKI)|
|[Historical Test-time Prompt Tuning for Vision Foundation Models](https://arxiv.org/pdf/2410.20346)|NeurIPS 2024|–|


















#### Transfer with Visual Prompt Tuning

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[Exploring Visual Prompts for Adapting Large-Scale Models](https://arxiv.org/abs/2203.17274)|arXiv 2022|[Code](https://github.com/hjbahng/visual_prompting)|
|[Retrieval-Enhanced Visual Prompt Learning for Few-shot Classification](https://arxiv.org/abs/2306.02243)|arXiv 2023|-|
|[Fine-Grained Visual Prompting](https://arxiv.org/abs/2306.04356)|arXiv 2023|-|
|[LoGoPrompt: Synthetic Text Images Can Be Good Visual Prompts for Vision-Language Models](https://arxiv.org/pdf/2309.01155v1.pdf)|ICCV 2023|[Code](https://chengshiest.github.io/logo/)|
|[Progressive Visual Prompt Learning with Contrastive Feature Re-formation](https://arxiv.org/abs/2304.08386)|IJCV 2024|[Code](https://github.com/MCG-NJU/ProVP)|
|[Visual In-Context Prompting](https://arxiv.org/abs/2311.13601)|CVPR 2024|[Code](https://github.com/UX-Decoder/DINOv)|
|[FALIP: Visual Prompt as Foveal Attention Boosts CLIP Zero-Shot Performance](https://arxiv.org/abs/2407.05578v1)|ECCV 2024|[Code](https://pumpkin805.github.io/FALIP/)|




#### Transfer with Text and Visual Prompt Tuning

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[UPT: Unified Vision and Language Prompt Learning](https://arxiv.org/abs/2210.07225)|arXiv 2022|[Code](https://github.com/yuhangzang/upt)|
|[MVLPT: Multitask Vision-Language Prompt Tuning](https://arxiv.org/abs/2211.11720)|arXiv 2022|[Code](https://github.com/facebookresearch/vilbert-multi-task)|
|[CAVPT: Dual Modality Prompt Tuning for Vision-Language Pre-Trained Model](https://arxiv.org/abs/2208.08340)|arXiv 2022|[Code](https://github.com/fanrena/DPT)|
|[MaPLe: Multi-modal Prompt Learning](https://arxiv.org/abs/2210.03117)|CVPR 2023|[Code](https://github.com/muzairkhattak/multimodal-prompt-learning)|
|[Learning to Prompt Segment Anything Models](https://arxiv.org/pdf/2401.04651.pdf)|arXiv 2024|-|
|[An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models](https://openreview.net/pdf?id=nc5GgFAvtk)|ICLR 2024|-|
|[GalLoP: Learning Global and Local Prompts for Vision-Language Models](https://arxiv.org/pdf/2407.01400)|ECCV 2024|-|
|[CLAP: Isolating Content from Style through Contrastive Learning with Augmented Prompts](https://arxiv.org/abs/2311.16445)|ECCV 2024|[Code](https://github.com/YichaoCai1/CLAP)|
|[Learning to Prompt Segment Anything Models](https://arxiv.org/pdf/2401.04651.pdf)|arXiv 2024|–|





### Transfer with Feature Adapter

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[Clip-Adapter: Better Vision-Language Models with Feature Adapters](https://arxiv.org/abs/2110.04544)|arXiv 2021|[Code](https://github.com/gaopengcuhk/CLIP-Adapter)|
|[Tip-Adapte: Training-free Adaption of CLIP for Few-shot Classification](https://arxiv.org/abs/2207.09519)|ECCV 2022|[Code](https://github.com/gaopengcuhk/Tip-Adapter)|
|[SVL-Adapter: Self-Supervised Adapter for Vision-Language Pretrained Models](https://arxiv.org/abs/2210.03794)|BMVC 2022|[Code](https://github.com/omipan/svl_adapter)|
|[CLIPPR: Improving Zero-Shot Models with Label Distribution Priors](https://arxiv.org/abs/2212.00784)|arXiv 2022|[Code](https://github.com/jonkahana/CLIPPR)|
|[SgVA-CLIP: Semantic-guided Visual Adapting of Vision-Language Models for Few-shot Image Classification](https://arxiv.org/abs/2211.16191)|arXiv 2022|-|
|[SuS-X: Training-Free Name-Only Transfer of Vision-Language Models](https://arxiv.org/abs/2211.16198)|ICCV 2023|[Code](https://github.com/vishaal27/SuS-X)|
|[VL-PET: Vision-and-Language Parameter-Efficient Tuning via Granularity Control](https://arxiv.org/abs/2308.09804)|ICCV 2023|[Code](https://github.com/HenryHZY/VL-PET)|
|[SAM-Adapter: Adapting SAM in Underperformed Scenes: Camouflage, Shadow, Medical Image Segmentation, and More](https://arxiv.org/abs/2304.09148)|arXiv 2023|[Code](http://tianrun-chen.github.io/SAM-Adaptor/)|
|[Segment Anything in High Quality](https://arxiv.org/abs/2306.01567)|arXiv 2023|[Code](https://github.com/SysCV/SAM-HQ)|
|[HGCLIP: Exploring Vision-Language Models with Graph Representations for Hierarchical Understanding](https://arxiv.org/abs/2311.14064)|COLING 2025|[Code](https://github.com/richard-peng-xia/HGCLIP)|
|[CLAP: Contrastive Learning with Augmented Prompts for Robustness on Pretrained Vision-Language Models](https://arxiv.org/abs/2311.16445)|arXiv 2023|-|
|[AWT: Transferring Vision-Language Models via Augmentation, Weighting, and Transportation](https://arxiv.org/abs/2407.04603)|NeurIPS 2024|[Code](https://github.com/MCG-NJU/AWT)|
|[A Closer Look at the Few-Shot Adaptation of Large Vision-Language Models](https://arxiv.org/abs/2312.12730)|CVPR 2024|[Code](https://github.com/jusiro/CLAP)|
|[Efficient Test-Time Adaptation of Vision-Language Models](https://arxiv.org/abs/2403.18293v1)|CVPR 2024|[Code](https://kdiaaa.github.io/tda/)|
|[Dual Memory Networks: A Versatile Adaptation Approach for Vision-Language Models](https://arxiv.org/abs/2403.17589v1)|CVPR 2024|[Code](https://github.com/YBZh/DMN)|



### Transfer with Other Methods

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[VT-Clip: Enhancing Vision-Language Models with Visual-guided Texts](https://arxiv.org/abs/2112.02399)|arXiv 2021|-|
|[Wise-FT: Robust fine-tuning of zero-shot models](https://arxiv.org/abs/2109.01903)|CVPR 2022|[Code](https://github.com/mlfoundations/wise-ft)|
|[MaskCLIP: Extract Free Dense Labels from CLIP](https://arxiv.org/abs/2112.01071)|ECCV 2022|[Code](https://github.com/chongzhou96/MaskCLIP)|
|[MUST: Masked Unsupervised Self-training for Label-free Image Classification](https://arxiv.org/abs/2206.02967)|ICLR 2023| [Code](https://github.com/salesforce/MUST)|
|[CALIP: Zero-Shot Enhancement of CLIP with Parameter-free Attention](https://arxiv.org/abs/2209.14169)|AAAI 2023|[Code](https://github.com/ziyuguo99/calip)|
|[Semantic Prompt for Few-Shot Image Recognition](https://arxiv.org/abs/2303.14123v1)|CVPR 2023|-|
|[Prompt, Generate, then Cache: Cascade of Foundation Models makes Strong Few-shot Learners](https://arxiv.org/abs/2303.02151)|CVPR 2023|[Code](https://github.com/ZrrSkywalker/CaFo)|
|[Task Residual for Tuning Vision-Language Models](https://arxiv.org/abs/2211.10277)|CVPR 2023|[Code](https://github.com/geekyutao/TaskRes)|
|[Deeply Coupled Cross-Modal Prompt Learning](https://arxiv.org/abs/2305.17903)|ACL 2023|[Code](https://github.com/GingL/CMPA)|
|[Prompt Ensemble Self-training for Open-Vocabulary Domain Adaptation](https://arxiv.org/abs/2306.16658)|arXiv 2023|-|
|[Personalize Segment Anything Model with One Shot](https://arxiv.org/abs/2305.03048)|arXiv 2023|[Code](https://github.com/ZrrSkywalker/Personalize-SAM)|
|[Chils: Zero-shot image classification with hierarchical label sets](https://proceedings.mlr.press/v202/novack23a/novack23a.pdf)|ICML 2023|[Code](https://github.com/acmi-lab/CHILS)|
|[Improving Zero-shot Generalization and Robustness of Multi-modal Models](https://openaccess.thecvf.com/content/CVPR2023/papers/Ge_Improving_Zero-Shot_Generalization_and_Robustness_of_Multi-Modal_Models_CVPR_2023_paper.pdf)|CVPR 2023|[Code](https://github.com/gyhandy/Hierarchy-CLIP)|
|[Exploiting Category Names for Few-Shot Classification with Vision-Language Models](https://openreview.net/pdf?id=w25Q9Ttjrs)|ICLR W 2023|-|
|[Beyond Sole Strength: Customized Ensembles for Generalized Vision-Language Models](https://arxiv.org/abs/2311.17091)|arXiv 2023|[Code](https://github.com/zhiheLu/Ensemble_VLM)|
|[Regularized Mask Tuning: Uncovering Hidden Knowledge in Pre-trained Vision-Language Models](https://arxiv.org/pdf/2307.15049v1.pdf)|ICCV 2023|[Code](https://wuw2019.github.io/RMT/)|
|[PromptStyler: Prompt-driven Style Generation for Source-free Domain Generalization](https://arxiv.org/pdf/2307.15199v1.pdf)|ICCV 2023|[Code](https://promptstyler.github.io/)|
|[PADCLIP: Pseudo-labeling with Adaptive Debiasing in CLIP for Unsupervised Domain Adaptation](https://assets.amazon.science/ff/08/64f27eb54b82a0c59c95dc138af4/padclip-pseudo-labeling-with-adaptive-debiasing-in-clip.pdf)|ICCV 2023|-|
|[Black Box Few-Shot Adaptation for Vision-Language models](https://arxiv.org/pdf/2304.01752.pdf)|ICCV 2023|[Code](https://github.com/saic-fi/LFA)|
|[AD-CLIP: Adapting Domains in Prompt Space Using CLIP](https://arxiv.org/pdf/2308.05659.pdf)|ICCVW 2023|-|
|[Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://arxiv.org/pdf/2306.14565.pdf)|arXiv 2023|[Code](https://fuxiaoliu.github.io/LRV/)|
|[Language Models as Black-Box Optimizers for Vision-Language Models](https://arxiv.org/abs/2309.05950)|arXiv 2023|-|
|[Matcher: Segment Anything with One Shot Using All-Purpose Feature Matching](https://arxiv.org/abs/2305.13310)|ICLR 2024|[Code](https://github.com/aim-uofa/Matcher)|
|[Consistency-guided Prompt Learning for Vision-Language Models](https://arxiv.org/abs/2306.01195)|ICLR 2024|-|
|[Efficient Test-Time Adaptation of Vision-Language Models](https://arxiv.org/abs/2403.18293v1)|CVPR 2024|[Code](https://kdiaaa.github.io/tda/)|
|[Dual Memory Networks: A Versatile Adaptation Approach for Vision-Language Models](https://arxiv.org/abs/2403.17589v1)|CVPR 2024|[Code](https://github.com/YBZh/DMN)|
|[A Closer Look at the Few-Shot Adaptation of Large Vision-Language Models](https://arxiv.org/abs/2312.12730)|CVPR 2024|[Code](https://github.com/jusiro/CLAP)|
|[Anchor-based Robust Finetuning of Vision-Language Models](https://arxiv.org/abs/2404.06244)|CVPR 2024||
|[Pre-trained Vision and Language Transformers Are Few-Shot Incremental Learners](https://arxiv.org/abs/2404.02117v1)|CVPR 2024|[Code](https://github.com/KHU-AGI/PriViLege)|













## Vision-Language Model Knowledge Distillation Methods

### Knowledge Distillation for Object Detection
| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[ViLD: Open-vocabulary Object Detection via Vision and Language Knowledge Distillation](https://arxiv.org/abs/2104.13921)|ICLR 2022|[Code](https://github.com/tensorflow/tpu/tree/master/models/official/detection/projects/vild)|
|[DetPro: Learning to Prompt for Open-Vocabulary Object Detection with Vision-Language Model](https://arxiv.org/abs/2203.14940)|CVPR 2022|[Code](https://github.com/dyabel/detpro)|
|[XPM: Open-Vocabulary Instance Segmentation via Robust Cross-Modal Pseudo-Labeling](https://arxiv.org/abs/2111.12698)|CVPR 2022|[Code](https://github.com/hbdat/cvpr22_cross_modal_pseudo_labeling)|
|[Bridging the Gap between Object and Image-level Representations for Open-Vocabulary Detection](https://arxiv.org/abs/2207.03482)|NeurIPS 2022|[Code](https://github.com/hanoonaR/object-centric-ovd)|
|[PromptDet: Towards Open-vocabulary Detection using Uncurated Images](https://arxiv.org/abs/2203.16513)|ECCV 2022|[Code](https://github.com/fcjian/PromptDet)|
|[PB-OVD: Open Vocabulary Object Detection with Pseudo Bounding-Box Labels](https://arxiv.org/abs/2111.09452)|ECCV 2022|[Code](https://github.com/salesforce/PB-OVD)|
|[OV-DETR: Open-Vocabulary DETR with Conditional Matching](https://arxiv.org/abs/2203.11876)|ECCV 2022|[Code](https://github.com/yuhangzang/OV-DETR)|
|[Detic: Detecting Twenty-thousand Classes using Image-level Supervision](https://arxiv.org/abs/2201.02605)|ECCV 2022|[Code](https://github.com/facebookresearch/Detic)|
|[OWL-ViT: Simple Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/abs/2205.06230)|ECCV 2022|[Code](https://github.com/google-research/scenic/tree/main/scenic/projects/owl_vit)|
|[VL-PLM: Exploiting Unlabeled Data with Vision and Language Models for Object Detection](https://arxiv.org/abs/2207.08954)|ECCV 2022|[Code](https://github.com/xiaofeng94/VL-PLM)|
|[ZSD-YOLO: Zero-shot Object Detection Through Vision-Language Embedding Alignment](https://arxiv.org/abs/2109.12066)|arXiv 2022|[Code](https://github.com/Johnathan-Xie/ZSD-YOLO)|
|[HierKD: Open-Vocabulary One-Stage Detection with Hierarchical Visual-Language Knowledge Distillation](https://arxiv.org/abs/2203.10593)|arXiv 2022|[Code](https://github.com/mengqiDyangge/HierKD)|
|[VLDet: Learning Object-Language Alignments for Open-Vocabulary Object Detection](https://arxiv.org/abs/2211.14843)|ICLR 2023|[Code](https://github.com/clin1223/VLDet)|
|[F-VLM: Open-Vocabulary Object Detection upon Frozen Vision and Language Models](https://arxiv.org/abs/2209.15639)|ICLR 2023|[Code](https://github.com/google-research/google-research/tree/master/fvlm)|
|[CondHead: Learning to Detect and Segment for Open Vocabulary Object Detection](https://arxiv.org/abs/2212.12130)|CVPR 2023|-|
|[Aligning Bag of Regions for Open-Vocabulary Object Detection](https://arxiv.org/abs/2302.13996)|CVPR 2023|[Code](https://github.com/wusize/ovdet)|
|[Region-Aware Pretraining for Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/abs/2305.07011v1)|CVPR 2023|[Code](https://github.com/mcahny/rovit)|
|[Object-Aware Distillation Pyramid for Open-Vocabulary Object Detection](https://arxiv.org/abs/2303.05892)|CVPR 2023|[Code](https://github.com/LutingWang/OADP)|
|[CORA: Adapting CLIP for Open-Vocabulary Detection with Region Prompting and Anchor Pre-Matching](https://arxiv.org/abs/2303.13076v1)|CVPR 2023|[Code](https://github.com/tgxs002/CORA)|
|[DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment](https://arxiv.org/abs/2304.04514v1)|CVPR 2023|-|
|[Detecting Everything in the Open World: Towards Universal Object Detection](https://arxiv.org/abs/2303.11749)|CVPR 2023|[Code](https://github.com/zhenyuw16/UniDetector)|
|[CapDet: Unifying Dense Captioning and Open-World Detection Pretraining](https://arxiv.org/abs/2303.02489)|CVPR 2023|-|
|[Contextual Object Detection with Multimodal Large Language Models](https://arxiv.org/abs/2305.18279)|arXiv 2023|[Code](https://github.com/yuhangzang/ContextDET)|
|[Building One-class Detector for Anything: Open-vocabulary Zero-shot OOD Detection Using Text-image Models](https://arxiv.org/abs/2305.17207)|arXiv 2023|[Code](https://github.com/gyhandy/One-Class-Anything)|
|[EdaDet: Open-Vocabulary Object Detection Using Early Dense Alignment](https://arxiv.org/pdf/2309.01151v1.pdf)|ICCV 2023|[Code](https://chengshiest.github.io/edadet)|
|[Improving Pseudo Labels for Open-Vocabulary Object Detection](https://arxiv.org/pdf/2308.06412.pdf)|arXiv 2023|-|
|[RegionGPT: Towards Region Understanding Vision Language Model](https://arxiv.org/pdf/2403.02330v1.pdf)|CVPR 2024|[Code](https://guoqiushan.github.io/regiongpt.github.io/)|
|[LLMs Meet VLMs: Boost Open Vocabulary Object Detection with Fine-grained Descriptors](https://arxiv.org/pdf/2402.04630.pdf)|ICLR 2024|-|
|[Ins-DetCLIP: Aligning Detection Model to Follow Human-Language Instruction](https://openreview.net/pdf?id=M0MF4t3hE9)|ICLR 2024|-|
|[Open-Vocabulary Object Detection via Language Hierarchy](https://arxiv.org/pdf/2410.20371)|NeurIPS 2024|–|





### Knowledge Distillation for Semantic Segmentation

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[SSIW: Semantic Segmentation In-the-Wild Without Seeing Any Segmentation Examples](https://arxiv.org/abs/2112.03185)|arXiv 2021|-|
|[ReCo: Retrieve and Co-segment for Zero-shot Transfer](https://arxiv.org/abs/2206.07045)|NeurIPS 2022|[Code](https://github.com/NoelShin/reco)|
|[CLIMS: Cross Language Image Matching for Weakly Supervised Semantic Segmentation](https://arxiv.org/abs/2203.02668)|CVPR 2022|[Code](https://github.com/CVI-SZU/CLIMS)|
|[CLIPSeg: Image Segmentation Using Text and Image Prompts](https://arxiv.org/abs/2112.10003)|CVPR 2022|[Code](https://github.com/timojl/clipseg)|
|[ZegFormer: Decoupling Zero-Shot Semantic Segmentation](https://arxiv.org/abs/2112.07910)|CVPR 2022|[Code](https://github.com/dingjiansw101/ZegFormer)|
|[LSeg: Language-driven Semantic Segmentation](https://arxiv.org/abs/2201.03546)|ICLR 2022|[Code](https://github.com/isl-org/lang-seg)|
|[ZSSeg: A Simple Baseline for Open-Vocabulary Semantic Segmentation with Pre-trained Vision-language Model](https://arxiv.org/abs/2112.14757)|ECCV 2022|[Code](https://github.com/MendelXu/zsseg.baseline)|
|[OpenSeg: Scaling Open-Vocabulary Image Segmentation with Image-Level Labels](https://arxiv.org/abs/2112.12143)|ECCV 2022|[Code](https://github.com/tensorflow/tpu/tree/641c1ac6e26ed788327b973582cbfa297d7d31e7/models/official/detection/projects/openseg)|
|[Fusioner: Open-vocabulary Semantic Segmentation with Frozen Vision-Language Models](https://arxiv.org/abs/2210.15138)|BMVC 2022|[Code](https://github.com/chaofanma/Fusioner)|
|[OVSeg: Open-Vocabulary Semantic Segmentation with Mask-adapted CLIP](https://arxiv.org/abs/2210.04150)|CVPR 2023|[Code](https://github.com/facebookresearch/ov-seg)|
|[ZegCLIP: Towards Adapting CLIP for Zero-shot Semantic Segmentation](https://arxiv.org/abs/2212.03588)|CVPR 2023|[Code](https://github.com/ZiqinZhou66/ZegCLIP)|
|[CLIP is Also an Efficient Segmenter: A Text-Driven Approach for Weakly Supervised Semantic Segmentation](https://arxiv.org/abs/2212.09506)|CVPR 2023|[Code](https://github.com/linyq2117/CLIP-ES)|
|[FreeSeg: Unified, Universal and Open-Vocabulary Image Segmentation](https://arxiv.org/abs/2303.17225v1)|CVPR 2023|[Code](https://freeseg.github.io/)|
|[Mask-free OVIS: Open-Vocabulary Instance Segmentation without Manual Mask Annotations](https://arxiv.org/abs/2303.16891v1)|CVPR 2023|[Code](https://vibashan.github.io/ovis-web/)|
|[Exploring Open-Vocabulary Semantic Segmentation without Human Labels](https://arxiv.org/abs/2306.00450)|arXiv 2023|-|
|[OpenVIS: Open-vocabulary Video Instance Segmentation](https://arxiv.org/abs/2305.16835)|arXiv 2023|-|
|[Segment Anything is A Good Pseudo-label Generator for Weakly Supervised Semantic Segmentation](https://arxiv.org/abs/2305.01275)|arXiv 2023|-|
|[Segment Anything Model (SAM) Enhanced Pseudo Labels for Weakly Supervised Semantic Segmentation](https://arxiv.org/abs/2305.05803)|arXiv 2023|[Code](https://github.com/cskyl/SAM_WSSS)|
|[Plug-and-Play, Dense-Label-Free Extraction of Open-Vocabulary Semantic Segmentation from Vision-Language Models](https://arxiv.org/abs/2311.17095)|arXiv 2023|-|
|[SegPrompt: Boosting Open-World Segmentation via Category-level Prompt Learning](https://arxiv.org/pdf/2308.06531v1.pdf)|ICCV 2023|[Code](https://github.com/aim-uofa/SegPrompt)|
|[ICPC: Instance-Conditioned Prompting with Contrastive Learning for Semantic Segmentation](https://arxiv.org/pdf/2308.07078.pdf)|arXiv 2023|-|
|[Convolutions Die Hard: Open-Vocabulary Segmentation with Single Frozen Convolutional CLIP](https://arxiv.org/pdf/2308.02487.pdf)|arXiv 2023|[Code](https://github.com/bytedance/fc-clip)|
|[Plug-and-Play, Dense-Label-Free Extraction of Open-Vocabulary Semantic Segmentation from Vision-Language Models](https://arxiv.org/abs/2311.17095)|arXiv 2023|-|
|[CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction](https://arxiv.org/abs/2310.01403)|ICLR 2024|-|



### Knowledge Distillation for Other Tasks

| Paper                                             |  Published in | Code/Project |                                  
|---------------------------------------------------|:-------------:|:------------:|
|[Controlling Vision-Language Models for Universal Image Restoration](https://arxiv.org/abs/2310.01018)|arXiv 2023|[Code](https://github.com/Algolzw/daclip-uir)|
|[FROSTER: Frozen CLIP Is A Strong Teacher for Open-Vocabulary Action Recognition](https://arxiv.org/pdf/2402.03241.pdf)|ICLR 2024|[Project](https://visual-ai.github.io/froster)|
|[AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection](https://arxiv.org/pdf/2310.18961.pdf)|ICLR 2024|[Code](https://github.com/zqhang/AnomalyCLIP)|
|[EXIF as Language: Learning Cross-Modal Associations Between Images and Camera Metadata](https://arxiv.org/abs/2301.04647)|CVPR 2023|[Code](https://hellomuffin.github.io/exif-as-language/)|




