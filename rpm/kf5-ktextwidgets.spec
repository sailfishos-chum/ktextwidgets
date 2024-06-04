%global kf5_version 5.108.0

Name: opt-kf5-ktextwidgets
Version: 5.108.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon with advanced text editing widgets

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/ktextwidgets
Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-kcompletion-devel >= %{kf5_version}
BuildRequires: opt-kf5-kconfig-devel >= %{kf5_version}
BuildRequires: opt-kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires: opt-kf5-ki18n-devel >= %{kf5_version}
BuildRequires: opt-kf5-kiconthemes-devel >= %{kf5_version}
BuildRequires: opt-kf5-kservice-devel >= %{kf5_version}
BuildRequires: opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-kwindowsystem-devel >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros
BuildRequires: opt-kf5-sonnet-devel >= %{kf5_version}

BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-kf5-kcompletion >= %{kf5_version}
Requires: opt-kf5-kconfigwidgets >= %{kf5_version}
Requires: opt-kf5-kconfig-gui >= %{kf5_version}
Requires: opt-kf5-ki18n >= %{kf5_version}
Requires: opt-kf5-sonnet-ui >= %{kf5_version}
Requires: opt-kf5-kwidgetsaddons >= %{kf5_version}

%description
KDE Frameworks 5 Tier 3 addon with advanced text edting widgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-kf5-ki18n-devel >= %{kf5_version}
Requires: opt-kf5-sonnet-devel >= %{kf5_version}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_libdir}/libKF5TextWidgets.so.*
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KTextWidgets/
%{_opt_kf5_libdir}/libKF5TextWidgets.so
%{_opt_kf5_libdir}/cmake/KF5TextWidgets/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KTextWidgets.pri
%{_opt_kf5_qtplugindir}/designer/*5widgets.so
