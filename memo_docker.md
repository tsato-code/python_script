# Docker �̍�Ǝ菇
- 2018-01-24
- Windows 10 Home �� Docker ���C���X�g�[�����ăR���e�i��� ubuntu ���g�����߂̎菇�B
- �z�X�g OS Windows 10 Home �œ���m�F


## �C���X�g�[��
- Docker ����L���F
https://qiita.com/maemori/items/52b1639fba4b1e68fccd
- �ȉ��̃y�[�W���� "Docker ToolBox on Windows" ���_�E�����[�h�A�C���X�g�[���ɏ]���F
https://docs.docker.com/toolbox/toolbox_install_windows/
- "Docker for Windows" ��Windows 10 Home �ɔ�Ή��ł��邱�Ƃɒ��ӁB


## �R���e�i��� ubuntu �𓮂���
- Docker Quickstart Terminal �𗧂��グ��B���ׂĂ����ő��삷�邱�Ƃ�O��ɂ���B
- �ȉ��R�}���h�� Docker ������ ubuntu �C���[�W�t�@�C����T���F
$ docker search ubuntu
- �ȉ��R�}���h�œK���ȃC���[�W�t�@�C���𗎂Ƃ��F
$ docker pull ubuntu
- �ȉ��R�}���h�ŃC���[�W�t�@�C���𗎂Ƃ������Ƃ��m�F�F
$ docker images
- �ȉ��R�}���h�� ubuntu �̃R���e�i�쐬�E�N���i--name �R���e�i�̖��O�͏ȗ��j�F
$ docker run -it -- name �R���e�i�� ubuntu bash
- �ȉ��R�}���h�ŃR���e�i���~���邱�ƂȂ��A�R���e�i���甲����F
$ ctrl+p ctrl+q
- �ȉ��R�}���h�ŃR���e�i��~�A�R���e�i���甲����F
$ exit
- �ȉ��R�}���h�ŁA�N�����̃R���e�i�� Docker �������~�E�N���ł���F
$ docker stop �R���e�i��
$ docker start �R���e�i��
- Docker ����ȉ��R�}���h�ŃR���e�i�ғ��󋵂��m�F�F
$ docker ps
- �ȉ��R�}���h�ŁA�N������ ubuntu �R���e�i�ɓ����� bash ��@���F
$ docker exec -it �R���e�i�� bash
- �ȉ��R�}���h�ŃR���e�i�̍폜�F
$ docker rm �R���e�iID
- �ȉ��R�}���h�ŃR���e�i�̈ꊇ�폜�F
$ docker rm `docker ps -aq`


## �R���e�i�Ɋ��蓖�Ă� CPU �R�A���⃁��������̒l��ύX
- �f�t�H���g��1�R�A1024MB�̊��蓖�ĂɂȂ�͂��B�����ύX����B
- �܂��A "Docker ToolBox for Windows" �Ɠ����ɃC���X�g�[�����ꂽ "Oracle VM VirtualBox" �� GUI �ŗ����グ��B
- �N������ VM �i"default" �Ƃ������O�����Ă���͂��j���~�����A�ݒ�u�V�X�e���v����^�u�u�}�U�[�{�[�h(M)�v�̃��C���������[�̃X���C�h�o�[�ƁA�^�u�u�v���Z�b�T�[(P)�v�̃v���Z�b�T�[���̃X���C�h�o�[�����ꂼ��K���Ȓl�ɑ��삷��B
- �R���e�i�N�����Ɉȉ��̃R�}���h�����s�F
$ docker run -m 25600m -it ubuntu bash
- �^�[�~�i������ȉ��̃R�}���h�Ŋ��蓖�Ă�ꂽ�R�A�����m�F�F
$ cat /proc/cpuinfo | grep processor
- �R���e�i�N�����ɃR�A�����w�肵�Ȃ��Ă��AVirtualBox �Ŏw�肵���l�������I�Ɋ��蓖�Ă���B
- CPU �R�A���ׂ̍����w����@���ȉ��̃y�[�W�ɏ�����Ă��邪�A�ǂ������܂������Ȃ��F
https://qiita.com/Yuhsak/items/d1438d83e480a93423c9


## �z�X�g OS �ƃR���e�i��� ubuntu �̋��L�t�H���_�쐬
- ��{�I�ɂ̓R���e�i�쐬���Ƀ}�E���g����B
- �i�P�j�C���X�g�[���ɏ]���ăC���X�g�[������ƁA�f�t�H���g�ł̓z�X�g�� Users �f�B���N�g���ȉ������}�E���g�ł��Ȃ��͂��F
$ docker run -v /c/Users/tsk_sato/share_test:/tmp/data -it ubuntu /bin/bash
- �i�Q�j�z�X�g���� Users �z���ɂȂ��f�B���N�g�����}�E���g����ɂ� VirtualBox �𑀍삷��B
- �Q�l�y�[�W�F
https://qiita.com/dojineko/items/f623894ef2436bef890e
- �܂��A "Docker ToolBox for Windows" �Ɠ����ɃC���X�g�[�����ꂽ "Oracle VM VirtualBox" �� GUI �ŗ����グ��B
- �N������ VM �i"default" �Ƃ������O�����Ă���͂��j�́A�ݒ�u���L�t�H���_�v���狤�L�t�H���_�[���X�g�� D �h���C�u��ǉ����A�K���ȃt�H���_�[���i�����ł� D_DRIVE �Ƃ������O�j�����A�u�����}�E���g�v�u�i��������v�̃`�F�b�N�{�b�N�X�Ƀ`�F�b�N���Ă����B
- ���� Docker Quickstart Terminal ����ȉ��̃R�}���h�F
$ docker-machine ssh default 'sudo mkdir -p /d'
$ docker-machine ssh default 'sudo mount -t vboxsf -o uid=0,gid=0 D_DRIVE /d'
- �Ō�ɁA�R���e�i�N������ D �h���C�u�͈ȉ��̃f�B���N�g�����w��F
$ docker run -v /d/share:/mnt/share -it --name TEST_SHARE ubuntu bash
- ��̋��L�t�H���_�ݒ�́AVirtualBox ����~����ƃ}�E���g���؂��悤���B�Ȃ̂ŁiDocker �̗��œ����Ă���j VirtualBox ���N�����邽�тɓ����悤�ɐݒ肷��K�v�����邩������Ȃ��B


## ubuntu �R���e�i�Ƀp�b�P�[�W���C���X�g�[��
- �ȉ��R�}���h�� apt-get �̃A�b�v�f�[�g�i��������Ȃ��ƃp�b�P�[�W�̃C���X�g�[�����ł��Ȃ������j�F
$ apt-get update
- �ȉ��R�}���h�� python �֘A�̃p�b�P�[�W�ꗗ�\���F
$ apt-cache search python
- �ȉ��R�}���h�� python3 ���C���X�g�[���F
$ apt-get install -y python3
$ apt-get install -y python3-pip
- �Ⴆ�Έȉ��R�}���h�� pip ���� PyTorch ���C���X�g�[���ł���F
$ pip3 install http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl 
$ pip3 install torchvision


## python ������{���������悤�ɂ���
- ubuntu �R���\�[������ python ���s���ɕ����R�[�h�G���[���N�����Ȃ��悤�Ɉȉ���ݒ�F
$ apt-get install language-pack-ja
$ export LANG=ja_JP.UTF-8
$ update-locale LANG=ja_JP.UTF-8


## �z�X�g OS ����R���e�i��� ubuntu �� python �𓮂���
- �Ⴆ�΁A�ȉ��R�}���h�ŊȒP�ȕ����o�͂ł���F
$ docker exec �R���e�i�� python3 -c "print('hogehoge')"
- �ȉ��R�}���h�� python �̃C���^�v���^�N���F
$ docker exec -it �R���e�i�� python3
- �ȉ��R�}���h�ŃR���e�i��� ubuntu �ɒu���ꂽ python �X�N���v�g�����s�F
$ docker exec �R���e�i�� python3 /ubuntu�f�B���N�g��/�X�N���v�g.py
- �ȉ��R�}���h�ŃR���e�i��� ubuntu �ɒu���ꂽ python �X�N���v�g�𕶎��R�[�h�w�肵�Ď��s�F
$ docker exec -e LANG=ja_JP.UTF-8 �R���e�i�� python3 /ubuntu�f�B���N�g��/�X�N���v�g.py


## �R���e�i�̈ڐA
- �R���e�i�� ubuntu ���J�X�^�}�C�Y�������̂��A�ق��̃}�V���ł��ȒP�Ɏg����悤�ɂ���ɂ͂��������@������B
- �i�P�j�ȉ��̓R���e�i���� Docker �C���[�W���쐬������@�B
- �Ⴆ�΁A�ȉ��̃R�}���h�Œ�~���̃R���e�i���� Docker �C���[�W���쐬�ł���i���|�W�g�����͐V�������� Docker �C���[�W�̖��O�̂��ƁA�^�O�����ȗ������ꍇ�� latest �ɂȂ�j�F
$ docker commit �R���e�i�� ���|�W�g����:�^�O��
- �Ⴆ�΁A�ȉ��̃R�}���h�ō쐬���� Docker �C���[�W����R���e�i�����F
$ docker run -it ���|�W�g����:�^�O�� bash
- ���Ƃ� DockerHub �� push ����΂悢�炵���B
- �i�Q�j�ȉ��̓R���e�i���� tar �t�@�C����f���o���ēǂݍ��ޕ��@�B
- �Ⴆ�΁A�ȉ��̃R�}���h�Œ�~���̃R���e�i�� tar �ɓf���o���ł���F
$ docker export �R���e�i�� > test.tar
- �ȉ��̃R�}���h�� tar ��ǂݍ��݂ł���i���|�W�g������ Docker �C���[�W�̖��O�̂��ƁA�^�O�����ȗ������ꍇ�� latest �ɂȂ�j�F
$ cat test.tar | docker import - ���|�W�g����:�^�O��
- �i�R�j�ق��� Dockerfile ���� Docker �C���[�W�� build ������@�����邪�����B
