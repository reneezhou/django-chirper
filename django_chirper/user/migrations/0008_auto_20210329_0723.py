# Generated by Django 3.1.5 on 2021-03-29 07:23

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210316_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country_code',
            field=models.CharField(choices=[[None, ''], ['+1', '+1 United States'], ['+1', '+1 Antigua and Barbuda'], ['+1', '+1 Anguilla'], ['+1', '+1 American Samoa'], ['+1', '+1 Barbados'], ['+1', '+1 Bermuda'], ['+1', '+1 Bahamas'], ['+1', '+1 Canada'], ['+1', '+1 Dominica'], ['+1', '+1 Dominican Republic'], ['+1', '+1 Grenada'], ['+1', '+1 Guam'], ['+1', '+1 Jamaica'], ['+1', '+1 Saint Kitts and Nevis'], ['+1', '+1 Cayman Islands'], ['+1', '+1 Saint Lucia'], ['+1', '+1 Northern Mariana Islands'], ['+1', '+1 Montserrat'], ['+1', '+1 Puerto Rico'], ['+1', '+1 Sint Maarten (Dutch part)'], ['+1', '+1 Turks and Caicos Islands'], ['+1', '+1 Trinidad and Tobago'], ['+1', '+1 Saint Vincent and the Grenadines'], ['+1', '+1 Virgin Islands'], ['+1', '+1 Virgin Islands'], ['+7', '+7 Russian Federation'], ['+7', '+7 Kazakhstan'], ['+20', '+20 Egypt'], ['+27', '+27 South Africa'], ['+30', '+30 Greece'], ['+31', '+31 Netherlands'], ['+32', '+32 Belgium'], ['+33', '+33 France'], ['+34', '+34 Spain'], ['+36', '+36 Hungary'], ['+39', '+39 Italy'], ['+39', '+39 Holy See (Vatican City State)'], ['+40', '+40 Romania'], ['+41', '+41 Switzerland'], ['+43', '+43 Austria'], ['+44', '+44 United Kingdom'], ['+44', '+44 Guernsey'], ['+44', '+44 Isle of Man'], ['+44', '+44 Jersey'], ['+45', '+45 Denmark'], ['+46', '+46 Sweden'], ['+47', '+47 Norway'], ['+47', '+47 Svalbard and Jan Mayen'], ['+48', '+48 Poland'], ['+49', '+49 Germany'], ['+51', '+51 Peru'], ['+52', '+52 Mexico'], ['+53', '+53 Cuba'], ['+54', '+54 Argentina'], ['+55', '+55 Brazil'], ['+56', '+56 Chile'], ['+57', '+57 Colombia'], ['+58', '+58 Venezuela'], ['+60', '+60 Malaysia'], ['+61', '+61 Australia'], ['+61', '+61 Cocos (Keeling) Islands'], ['+61', '+61 Christmas Island'], ['+62', '+62 Indonesia'], ['+63', '+63 Philippines'], ['+64', '+64 New Zealand'], ['+65', '+65 Singapore'], ['+66', '+66 Thailand'], ['+81', '+81 Japan'], ['+82', '+82 Korea'], ['+84', '+84 Viet Nam'], ['+86', '+86 China'], ['+90', '+90 Turkey'], ['+91', '+91 India'], ['+92', '+92 Pakistan'], ['+93', '+93 Afghanistan'], ['+94', '+94 Sri Lanka'], ['+95', '+95 Myanmar'], ['+98', '+98 Iran'], ['+211', '+211 South Sudan'], ['+212', '+212 Morocco'], ['+212', '+212 Western Sahara'], ['+213', '+213 Algeria'], ['+216', '+216 Tunisia'], ['+218', '+218 Libya'], ['+220', '+220 Gambia'], ['+221', '+221 Senegal'], ['+222', '+222 Mauritania'], ['+223', '+223 Mali'], ['+224', '+224 Guinea'], ['+225', "+225 Côte d'Ivoire"], ['+226', '+226 Burkina Faso'], ['+227', '+227 Niger'], ['+228', '+228 Togo'], ['+229', '+229 Benin'], ['+230', '+230 Mauritius'], ['+231', '+231 Liberia'], ['+232', '+232 Sierra Leone'], ['+233', '+233 Ghana'], ['+234', '+234 Nigeria'], ['+235', '+235 Chad'], ['+236', '+236 Central African Republic'], ['+237', '+237 Cameroon'], ['+238', '+238 Cabo Verde'], ['+239', '+239 Sao Tome and Principe'], ['+240', '+240 Equatorial Guinea'], ['+241', '+241 Gabon'], ['+242', '+242 Congo'], ['+243', '+243 Congo'], ['+244', '+244 Angola'], ['+245', '+245 Guinea-Bissau'], ['+246', '+246 British Indian Ocean Territory'], ['+248', '+248 Seychelles'], ['+249', '+249 Sudan'], ['+250', '+250 Rwanda'], ['+251', '+251 Ethiopia'], ['+252', '+252 Somalia'], ['+253', '+253 Djibouti'], ['+254', '+254 Kenya'], ['+255', '+255 Tanzania'], ['+256', '+256 Uganda'], ['+257', '+257 Burundi'], ['+258', '+258 Mozambique'], ['+260', '+260 Zambia'], ['+261', '+261 Madagascar'], ['+262', '+262 Réunion'], ['+262', '+262 Mayotte'], ['+263', '+263 Zimbabwe'], ['+264', '+264 Namibia'], ['+265', '+265 Malawi'], ['+266', '+266 Lesotho'], ['+267', '+267 Botswana'], ['+268', '+268 Eswatini'], ['+269', '+269 Comoros'], ['+290', '+290 Saint Helena'], ['+291', '+291 Eritrea'], ['+297', '+297 Aruba'], ['+298', '+298 Faroe Islands'], ['+299', '+299 Greenland'], ['+350', '+350 Gibraltar'], ['+351', '+351 Portugal'], ['+352', '+352 Luxembourg'], ['+353', '+353 Ireland'], ['+354', '+354 Iceland'], ['+355', '+355 Albania'], ['+356', '+356 Malta'], ['+357', '+357 Cyprus'], ['+358', '+358 Finland'], ['+358', '+358 Åland Islands'], ['+359', '+359 Bulgaria'], ['+370', '+370 Lithuania'], ['+371', '+371 Latvia'], ['+372', '+372 Estonia'], ['+373', '+373 Moldova'], ['+374', '+374 Armenia'], ['+375', '+375 Belarus'], ['+376', '+376 Andorra'], ['+377', '+377 Monaco'], ['+378', '+378 San Marino'], ['+380', '+380 Ukraine'], ['+381', '+381 Serbia'], ['+382', '+382 Montenegro'], ['+385', '+385 Croatia'], ['+386', '+386 Slovenia'], ['+387', '+387 Bosnia and Herzegovina'], ['+389', '+389 North Macedonia'], ['+420', '+420 Czechia'], ['+421', '+421 Slovakia'], ['+423', '+423 Liechtenstein'], ['+500', '+500 Falkland Islands (Malvinas)'], ['+501', '+501 Belize'], ['+502', '+502 Guatemala'], ['+503', '+503 El Salvador'], ['+504', '+504 Honduras'], ['+505', '+505 Nicaragua'], ['+506', '+506 Costa Rica'], ['+507', '+507 Panama'], ['+508', '+508 Saint Pierre and Miquelon'], ['+509', '+509 Haiti'], ['+590', '+590 Guadeloupe'], ['+590', '+590 Saint Barthélemy'], ['+590', '+590 Saint Martin (French part)'], ['+591', '+591 Bolivia'], ['+592', '+592 Guyana'], ['+593', '+593 Ecuador'], ['+594', '+594 French Guiana'], ['+595', '+595 Paraguay'], ['+596', '+596 Martinique'], ['+597', '+597 Suriname'], ['+598', '+598 Uruguay'], ['+599', '+599 Curaçao'], ['+599', '+599 Bonaire'], ['+670', '+670 Timor-Leste'], ['+672', '+672 Norfolk Island'], ['+673', '+673 Brunei Darussalam'], ['+674', '+674 Nauru'], ['+675', '+675 Papua New Guinea'], ['+676', '+676 Tonga'], ['+677', '+677 Solomon Islands'], ['+678', '+678 Vanuatu'], ['+679', '+679 Fiji'], ['+680', '+680 Palau'], ['+681', '+681 Wallis and Futuna'], ['+682', '+682 Cook Islands'], ['+683', '+683 Niue'], ['+685', '+685 Samoa'], ['+686', '+686 Kiribati'], ['+687', '+687 New Caledonia'], ['+688', '+688 Tuvalu'], ['+689', '+689 French Polynesia'], ['+690', '+690 Tokelau'], ['+691', '+691 Micronesia'], ['+692', '+692 Marshall Islands'], ['+850', '+850 Korea'], ['+852', '+852 Hong Kong'], ['+853', '+853 Macao'], ['+855', '+855 Cambodia'], ['+856', "+856 Lao People's Democratic Republic"], ['+880', '+880 Bangladesh'], ['+886', '+886 Taiwan'], ['+960', '+960 Maldives'], ['+961', '+961 Lebanon'], ['+962', '+962 Jordan'], ['+963', '+963 Syrian Arab Republic'], ['+964', '+964 Iraq'], ['+965', '+965 Kuwait'], ['+966', '+966 Saudi Arabia'], ['+967', '+967 Yemen'], ['+968', '+968 Oman'], ['+970', '+970 Palestine'], ['+971', '+971 United Arab Emirates'], ['+972', '+972 Israel'], ['+973', '+973 Bahrain'], ['+974', '+974 Qatar'], ['+975', '+975 Bhutan'], ['+976', '+976 Mongolia'], ['+977', '+977 Nepal'], ['+992', '+992 Tajikistan'], ['+993', '+993 Turkmenistan'], ['+994', '+994 Azerbaijan'], ['+995', '+995 Georgia'], ['+996', '+996 Kyrgyzstan'], ['+998', '+998 Uzbekistan']], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='handle',
            field=models.TextField(default=user.models.gen_hex, error_messages={'unique': 'That username has been taken. Please choose another.'}, unique=True),
        ),
    ]