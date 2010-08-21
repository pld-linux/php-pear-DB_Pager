%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	Pager
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - retrieve and return information of database result sets
Summary(pl.UTF-8):	%{_pearname} - pobieranie i zwracanie informacji o zestawacanie rezultatów z baz danych
Name:		php-pear-%{_pearname}
Version:	0.7.2
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e01f5092a2a95488dae09f2c8d2823b0
URL:		http://pear.php.net/package/DB_Pager/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class handles all the stuff needed for displaying paginated
results from a database query of PEAR DB, including fetching only the
needed rows and giving extensive information for helping build an HTML
or GTK+ query result display.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa obsługuje wszystko co potrzebne do wyświetlania
stronicowanych wyników z zapytania do bazy PEAR DB, włącznie ze
ściąganiem tylko potrzebnych wierszy i dawaniem szczegółowych
informacji pomocnych przy wyświetlaniu wyników zapytania w HTML-u lub
GTK+.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
