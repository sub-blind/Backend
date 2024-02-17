<h2>클라우드 컴퓨팅 개념 설명해보기</h2>

클라우드 컴퓨팅은 스토리지, 서버, 애플리케이션 등을 인터넷을 통해 제공하는 구축 모델입니다. 보통 종량제 결제 방식으로 온디맨드 및 서비스형으로 제공됩니다. ‘클라우드’는 물리적 장소가 아니라 로컬 시스템과 프라이빗 데이터 센터를 주로 대체하는 IT 리소스 관리 방식입니다.<br>
<br>사용자는 클라우드 컴퓨팅 모델에서 원격 공급자가 온라인으로 제공하는 가상 컴퓨팅, 네트워크, 스토리지 리소스에 액세스합니다. 광범위한 컴퓨팅, 스토리지 및 기타 IT 인프라를 구매 및 유지 관리할 필요가 없으며 관련 장비를 관리할 전문 지식 및 기술을 갖춘 사내 인력이 없어도 클라우드 서비스 공급자가 대부분의 부담을 대신 처리합니다.

<h2>리전, 가용 영역, 엣지 로케이션 개념 설명해보기</h2>
리전(Region)
    - 해당 지리적인 영역 내에서 격리되고 물리적으로 분리된 여러 개의 가용 영역의 모음 <br>
    - 최소 2개의 가용 영역으로 구성<br>
    - 예를 들어 가용 영역이 위치한 특정 지역에 물리적인 재난이나 재해로 서비스 이용이 불가능 할 수 있다.<br> 
    - 이를 극복하기 위해 AWS에 서비스를 구성할 때 가용 영역을 분산하여 구성하는 것을 권장<br>
<br>가용 영역(Availability zone) - 한 개 이상의 데이터 센터들의 모음 - 데이터 센터는 분산되어 있으며, 초고속 광통신 전용망으로 연결되어 있다.<br>
<br>엣지(Edge POP(Point of Presense)) - 외부 인터넷과 AWS 글로벌 네트워크망과 연결하는 별도의 센터 - 엣지 로케이션(Edge Location)과 리전별 엣지 캐시- (Regional Edge Cache)로 구성 - CloudFront와 같은 CDN 서비스의 데이터 캐시 기능을 제공

<h2>클라우드의 종류 설명해보기</h2>
<img src="./image/image.png">
On Premises(ownserver) - 기업이 자체적으로 IT 인프라를 소유, 관리 및 운영하는 경우를 ‘On premises’라고 합니다. - 이 경우 사내 IT 팀이 시스템의 설계, 구축 및 관리를 담당합니다. 드물지만, 서드 파티 공급업체가 일부 구성 요소를 관리하는 경우도 있습니다. 그러나 대부분의 경우 조직이 위치, 장치, 소프트웨어 및 애플리케이션을 완전히 소유하고 관리합니다.<br>

<br>IaaS 클라우드 서비스 - 스토리지, 컴퓨팅, 네트워크 기능에 대한 인프라 서비스를 제공하는 IaaS 플랫폼은 가상화 기술을 기반으로한 클라우드 서비스 유형입니다.

PaaS 클라우드 서비스 - 인프라 가상화 기반 위에 OS(운영체제), 런타임 환경 그리고 미들웨어 서비스를 추가로 구성한 클라우드 서비스 유형입니다.

SaaS 클라우드 서비스 - 이미 개발이 완료된 애플리케이션을 용도에 맞게 바로 사용할 수 있는 클라우드 서비스 유형입니다.