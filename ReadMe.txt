TurtleFollow

TurtleFollow, ROS 2 kullanarak Turtlesim simülasyon ortamında özel servisler oluşturma ve kullanma örneğini göstermek için tasarlanmış bir pakettir. Bu proje, iki ana servis içerir:

Kaplumbağa Oluşturma Servisi: Turtlesim ortamında dinamik olarak kaplumbağalar oluşturur.

Kaplumbağa Takip Servisi: Bir veya birden fazla kaplumbağanın hedef bir kaplumbağayı takip etmesini sağlar.

Gereksinimler

ROS 2 Humble veya daha yeni bir sürüm

Python 3.8+

Turtlesim paketi (sudo apt install ros-humble-turtlesim)

Kurulum

Depoyu klonlayın:

git clone https://github.com/yourusername/turtlefollow.git
cd turtlefollow

Workspace'i derleyin:

colcon build
source install/setup.bash

Kullanım

Kaplumbağa Oluşturma Servisi

Turtlesim düğümünü başlatın:

ros2 run turtlesim turtlesim_node

Kaplumbağa oluşturma servisini çalıştırın:

ros2 run turtlefollow turtle_creation_service

Servisi çağırıp kaplumbağalar oluşturun:

ros2 service call /turtles_create turtlefollow/srv/CreateTurtles "{count: 3}"

Kaplumbağa Takip Servisi

Kaplumbağa takip servisini çalıştırın:

ros2 run turtlefollow turtle_follow_service

Servisi çağırıp kaplumbağaları hedef bir kaplumbağayı takip ettirin:

ros2 service call /turtles_follow turtlefollow/srv/FollowTurtle "{target_name: 'turtle1'}"

Dosya Yapısı

├── turtlefollow
│   ├── __init__.py
│   ├── turtle_creation_service.py
│   ├── turtle_follow_service.py
├── srv
│   ├── CreateTurtles.srv
│   └── FollowTurtle.srv
├── package.xml
├── CMakeLists.txt
└── setup.py

turtle_creation_service.py: Kaplumbağa oluşturma mantığını içerir.

turtle_follow_service.py: Kaplumbağaları hedef bir kaplumbağayı takip etmeye yönelik mantığı uygular.

CreateTurtles.srv: Kaplumbağa oluşturma için özel bir servis.

FollowTurtle.srv: Kaplumbağa takip için özel bir servis.

Katkıda Bulunma

Bu depoyu forklayarak çekme isteğileri gönderebilirsiniz. Öneriler ve iyileştirmeler her zaman memnuniyetle karşılanır!

Destek

Sorularınız veya sorunlarınız için lütfen GitHub deposunda bir sorun (“issue”) oluşturun.

Bilgilendirme

Bu proje, ROS 2'de özel servislerin kullanımını göstermek için eğitim amaçlıdır.
