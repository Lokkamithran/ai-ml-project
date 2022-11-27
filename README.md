# Credit Card Approval using Machine Learning


married_status = ['Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow']

way_of_living = ['House / apartment', 'With parents', 'Municipal apartment', 'Rented apartment', 'Office apartment']


M-1, F-0
Y-1, N-0
*Commercial associate - 0.0, c*
*pensioner-0.25*
*State servant-0.5,*
 *student-0.75*
*Working-1.0*


*Academic degree - 0.0*
*,Higher education-0.25,c*
*Incop Higher - 0.5,*
*Lower secondary - 0.75*
*Secondary / secondary special-1*

*Civil marriage - 0*
*Married,-0.25 c*
*Separated - 0.5*
*Single / not married - 0.75*
*Widow-1*

*Co-op apartment-0*
*House / apartment, 0.2 c*
*Municipal apartment-0.4*
*Office apartment-0.6*
*Rented apartment - 0.8*
*With parents - 1*


# Will be approved, with percent chance

[Male, Y, Y, 3, 258750, Student, Higher Education, Widow, House/Apartment, 1393, 4], 82.2%
[Female, Y, Y, 1, 800000, Working, Academic Degree, Married, Rented Apartment, 5000, 3], approx 100%
[Female, Y, Y, 2, 150000, Working, Higher Education, Married, Municipal Apartment, 2000, 4], 97.7%
[Male, Y, N, 2, 123456, Pensioner, Higher Education, Civil Marriage, Co-op Apartment, 0, 4], 100%
<!-- [Male, N, N, 3, 50000, State Servant, Lower Secondary, Separated, Office Apartment, 365, 4], 100% -->
<!-- [Male, N, N, 3, 45000, Student, Incomplete Higher, Single, With Parents, 0, 4], 99.99% -->
<!-- [Female, N, N, 3, 45000, Student, Incomplete Higher, Single, With Parents, 0, 4], 99.99% -->
<!-- [Male, Y, Y, 2, 100000, Working, Higher Education, Widow, Minicipal Apartment, 1000, 3], 97.8% -->

# Won't be approved, with percent chance

[Female, Y, Y, 3, 258750, Student, Higher Education, Widow, House/Apartment, 1393, 4], 17.3%
[Female, Y, Y, 2, 150000, Student, Higher Education, Widow, House/Apartment, 2000, 4], 17.3%
[Female, N, N, 1, 258000, Student, Incomplete Higher, Widow, House/Apartment, 1500, 4], 17.3%
[Female, Y, Y, 2, 150000, Working, Higher Education, Widow, Municipal Apartment, 2000, 4], 17.3%
[Male, Y, Y, 2, 150000, Working, Higher Education, Widow, Municipal Apartment, 2000, 4], 17.3%
