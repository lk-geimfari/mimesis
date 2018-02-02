"""Provides all the generic data related to the address."""

COUNTRY_CODES = {
    'a2': [
        'AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AQ', 'AR', 'AS',
        'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH',
        'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY',
        'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN',
        'CO', 'CR', 'CU', 'CV', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO',
        'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM',
        'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM',
        'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN',
        'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS',
        'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP',
        'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT',
        'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML',
        'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX',
        'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR',
        'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN',
        'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA',
        'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN',
        'SO', 'SR', 'SS', 'ST', 'SV', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH',
        'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA',
        'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU',
        'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW',
    ],
    'a3': [
        'AND', 'ARE', 'AFG', 'ATG', 'AIA', 'ALB', 'ARM', 'ANT', 'AGO', 'ATA',
        'ARG', 'ASM', 'AUT', 'AUS', 'ABW', 'ALA', 'AZE', 'BIH', 'BRB', 'BGD',
        'BEL', 'BFA', 'BGR', 'BHR', 'BDI', 'BEN', 'BLM', 'BMU', 'BRN', 'BOL',
        'BRA', 'BHS', 'BTN', 'BVT', 'BWA', 'BLR', 'BLZ', 'CAN', 'CCK', 'COD',
        'CAF', 'COG', 'CHE', 'CIV', 'COK', 'CHL', 'CMR', 'CHN', 'COL', 'CRI',
        'CUB', 'CPV', 'CXR', 'CYP', 'CZE', 'DEU', 'DJI', 'DNK', 'DMA', 'DOM',
        'DZA', 'ECU', 'EST', 'EGY', 'ESH', 'ERI', 'ESP', 'ETH', 'FIN', 'FJI',
        'FLK', 'FSM', 'FRO', 'FRA', 'GAB', 'GBR', 'GRD', 'GEO', 'GUF', 'GGY',
        'GHA', 'GIB', 'GRL', 'GMB', 'GIN', 'GLP', 'GNQ', 'GRC', 'SGS', 'GTM',
        'GUM', 'GNB', 'GUY', 'HKG', 'HMD', 'HND', 'HRV', 'HTI', 'HUN', 'IDN',
        'IRL', 'ISR', 'IMN', 'IND', 'IOT', 'IRQ', 'IRN', 'ISL', 'ITA', 'JEY',
        'JAM', 'JOR', 'JPN', 'KEN', 'KGZ', 'KHM', 'KIR', 'COM', 'KNA', 'PRK',
        'KOR', 'KWT', 'CYM', 'KAZ', 'LAO', 'LBN', 'LCA', 'LIE', 'LKA', 'LBR',
        'LSO', 'LTU', 'LUX', 'LVA', 'LBY', 'MAR', 'MCO', 'MDA', 'MNE', 'MAF',
        'MDG', 'MHL', 'MKD', 'MLI', 'MMR', 'MNG', 'MAC', 'MNP', 'MTQ', 'MRT',
        'MSR', 'MLT', 'MUS', 'MDV', 'MWI', 'MEX', 'MYS', 'MOZ', 'NAM', 'NCL',
        'NER', 'NFK', 'NGA', 'NIC', 'NLD', 'NOR', 'NPL', 'NRU', 'NIU', 'NZL',
        'OMN', 'PAN', 'PER', 'PYF', 'PNG', 'PHL', 'PAK', 'POL', 'SPM', 'PCN',
        'PRI', 'PSE', 'PRT', 'PLW', 'PRY', 'QAT', 'REU', 'ROU', 'SRB', 'RUS',
        'RWA', 'SAU', 'SLB', 'SYC', 'SDN', 'SWE', 'SGP', 'SHN', 'SVN', 'SJM',
        'SVK', 'SLE', 'SMR', 'SEN', 'SOM', 'SUR', 'SSD', 'STP', 'SLV', 'SYR',
        'SWZ', 'TCA', 'TCD', 'ATF', 'TGO', 'THA', 'TJK', 'TKL', 'TLS', 'TKM',
        'TUN', 'TON', 'TUR', 'TTO', 'TUV', 'TWN', 'TZA', 'UKR', 'UGA', 'UMI',
        'USA', 'URY', 'UZB', 'VAT', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT',
        'WLF', 'WSM', 'YEM', 'MYT', 'ZAF', 'ZMB', 'ZWE',
    ],
    'fifa': [
        'AFG', 'AIA', 'ALB', 'ALG', 'AND', 'ANG', 'ARG', 'ARM', 'ARU', 'ARU',
        'ASA', 'ATG', 'AUT', 'AZE', 'BAH', 'BAN', 'BDI', 'BEL', 'BEN', 'BER',
        'BFA', 'BHR', 'BHU', 'BIH', 'BLR', 'BLZ', 'BOE', 'BOL', 'BOT', 'BRA',
        'BRB', 'BRU', 'BUL', 'CAM', 'CAN', 'CAY', 'CGO', 'CHA', 'CHI', 'CHN',
        'CIV', 'CMR', 'COD', 'COK', 'COL', 'COM', 'CPV', 'CRC', 'CRO', 'CTA',
        'CUB', 'CUW', 'CYP', 'CZE', 'DEN', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY',
        'ENG', 'EQG', 'ERI', 'ESP', 'EST', 'ETH', 'FIJ', 'FIN', 'FRA', 'FRO',
        'GAB', 'GAM', 'GEO', 'GER', 'GHA', 'GIB', 'GNB', 'GPE', 'GRE', 'GRN',
        'GUA', 'GUI', 'GUM', 'GUY', 'GYF', 'HAI', 'HKG', 'HON', 'HUN', 'IDN',
        'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN',
        'KAZ', 'KEN', 'KGZ', 'KIR', 'KOR', 'KSA', 'KUW', 'LAO', 'LBR', 'LBY',
        'LCA', 'LES', 'LIB', 'LIE', 'LTU', 'LUX', 'LVA', 'MAC', 'MAD', 'MAR',
        'MAS', 'MDA', 'MDV', 'MEX', 'MKD', 'MLI', 'MLT', 'MNE', 'MNG', 'MOZ',
        'MRI', 'MSR', 'MTN', 'MTQ', 'MWI', 'MYA', 'NAM', 'NCA', 'NCL', 'NED',
        'NEP', 'NGA', 'NIG', 'NIR', 'NIU', 'NMI', 'NOR', 'NZL', 'OMA', 'PAK',
        'PAN', 'PAR', 'PER', 'PHI', 'PLE', 'PNG', 'POL', 'POR', 'PRK', 'PUR',
        'QAT', 'REU', 'ROU', 'RSA', 'RUS', 'RWA', 'SAM', 'SCO', 'SDN', 'SEN',
        'SEY', 'SIN', 'SKN', 'SLE', 'SLV', 'SMR', 'SMT', 'SOL', 'SOM', 'SRB',
        'SRI', 'SSD', 'STP', 'SUI', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SXM',
        'SYR', 'TAH', 'TAN', 'TCA', 'TGA', 'THA', 'TJK', 'TKM', 'TLS', 'TOG',
        'TPE', 'TRI', 'TUN', 'TUR', 'TUV', 'UAE', 'UGA', 'UKR', 'URU', 'USA',
        'UZB', 'VAN', 'VEN', 'VGB', 'VIE', 'VIN', 'VIR', 'WAL', 'YEM', 'ZAM',
        'ZAN', 'ZIM',
    ],
    'ioc': [
        'AFG', 'ALB', 'ALG', 'AND', 'ANG', 'ANT', 'ARG', 'ARM', 'ARU', 'ASA',
        'AUS', 'AUT', 'AZE', 'BAH', 'BAN', 'BAR', 'BDI', 'BEL', 'BEN', 'BER',
        'BHU', 'BIH', 'BIZ', 'BLR', 'BOL', 'BOT', 'BRA', 'BRN', 'BRU', 'BUL',
        'BUR', 'CAF', 'CAM', 'CAN', 'CAY', 'CGO', 'CHA', 'CHI', 'CHN', 'CIV',
        'CMR', 'COD', 'COK', 'COL', 'COM', 'CPV', 'CRC', 'CRO', 'CUB', 'CYP',
        'CZE', 'DEN', 'DJI', 'DMA', 'DOM', 'ECU', 'EGY', 'ERI', 'ESA', 'ESP',
        'EST', 'ETH', 'FIJ', 'FIN', 'FRA', 'FSM', 'GAB', 'GAM', 'GBR', 'GBS',
        'GEO', 'GEQ', 'GER', 'GHA', 'GRE', 'GRN', 'GUA', 'GUI', 'GUM', 'GUY',
        'HAI', 'HKG', 'HON', 'HUN', 'INA', 'IND', 'IRI', 'IRL', 'IRQ', 'ISL',
        'ISR', 'ISV', 'ITA', 'IVB', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ',
        'KIR', 'KOR', 'KSA', 'KUW', 'LAO', 'LAT', 'LBA', 'LBR', 'LCA', 'LES',
        'LIB', 'LIE', 'LTU', 'LUX', 'MAD', 'MAR', 'MAS', 'MAW', 'MDA', 'MDV',
        'MEX', 'MGL', 'MHL', 'MKD', 'MLI', 'MLT', 'MNE', 'MON', 'MOZ', 'MRI',
        'MTN', 'MYA', 'NAM', 'NCA', 'NED', 'NEP', 'NGR', 'NIG', 'NOR', 'NRU',
        'NZL', 'OMA', 'PAK', 'PAN', 'PAR', 'PER', 'PHI', 'PLE', 'PLW', 'PNG',
        'POL', 'POR', 'PRK', 'PUR', 'QAT', 'ROU', 'RSA', 'RUS', 'RWA', 'SAM',
        'SEN', 'SEY', 'SIN', 'SKN', 'SLE', 'SLO', 'SMR', 'SOL', 'SOM', 'SRB',
        'SRI', 'STP', 'SUD', 'SUI', 'SUR', 'SVK', 'SWE', 'SWZ', 'SYR', 'TAN',
        'TGA', 'THA', 'TJK', 'TKM', 'TLS', 'TOG', 'TPE', 'TTO', 'TUN', 'TUR',
        'TUV', 'UAE', 'UGA', 'UKR', 'URU', 'USA', 'UZB', 'VAN', 'VEN', 'VIE',
        'VIN', 'YEM', 'ZAM', 'ZIM',
    ],
    'numeric': [
        '020', '784', '004', '028', '660', '008', '051', '530', '024',
        '010', '032', '016', '040', '036', '533', '248', '031', '070',
        '052', '050', '056', '854', '100', '048', '108', '204', '652',
        '060', '096', '068', '076', '044', '064', '074', '072', '112',
        '084', '124', '166', '180', '140', '178', '756', '384', '184',
        '152', '120', '156', '170', '188', '192', '132', '162', '196',
        '203', '276', '262', '208', '212', '214', '012', '218', '233',
        '818', '732', '232', '724', '231', '246', '242', '238', '583',
        '234', '250', '266', '826', '308', '268', '254', '831', '288',
        '292', '304', '270', '324', '312', '226', '300', '239', '320',
        '316', '624', '328', '344', '334', '340', '191', '332', '348',
        '360', '372', '376', '833', '356', '086', '368', '364', '352',
        '380', '832', '388', '400', '392', '404', '417', '116', '296',
        '174', '659', '408', '410', '414', '136', '398', '418', '422',
        '662', '438', '144', '430', '426', '440', '442', '428', '434',
        '504', '492', '498', '499', '663', '450', '584', '807', '466',
        '104', '496', '446', '580', '474', '478', '500', '470', '480',
        '462', '454', '484', '458', '508', '516', '540', '562', '574',
        '566', '558', '528', '578', '524', '520', '570', '554', '512',
        '591', '604', '258', '598', '608', '586', '616', '666', '612',
        '630', '275', '620', '585', '600', '634', '638', '642', '688',
        '643', '646', '682', '090', '690', '736', '752', '702', '654',
        '705', '744', '703', '694', '674', '686', '706', '740', '728',
        '678', '222', '760', '748', '796', '148', '260', '768', '764',
        '762', '772', '626', '795', '788', '776', '792', '780', '798',
        '158', '834', '804', '800', '581', '840', '858', '860', '336',
        '670', '862', '092', '850', '704', '548', '876', '882', '887',
        '175', '710', '894', '716',
    ],
}

SHORTENED_ADDRESS_FMT = [
    'cs',
    'da',
    'de',
    'de-at',
    'de-ch',
    'el',
    'es',
    'fi',
    'is',
    'nl',
    'nl-be',
    'no',
    'sv',
]

CONTINENT_CODES = ['AF', 'NA', 'OC', 'AN', 'AS', 'EU', 'SA']

CALLING_CODES = [
    '+1', '+7', '+20', '+27', '+30', '+31', '+32', '+33',
    '+34', '+36', '+39', '+40', '+41', '+43', '+44', '+44',
    '+44', '+44', '+45', '+46', '+47', '+48', '+49', '+51',
    '+52', '+53', '+54', '+55', '+56', '+56', '+57', '+58',
    '+60', '+61', '+61', '+61', '+62', '+63', '+64', '+64',
    '+64', '+65', '+66', '+77', '+81', '+82', '+84', '+86',
    '+90', '+91', '+92', '+93', '+94', '+95', '+98', '+211',
    '+212', '+213', '+216', '+218', '+220', '+221', '+222',
    '+223', '+224', '+225', '+226', '+227', '+228', '+229',
    '+230', '+231', '+232', '+233', '+234', '+235', '+236',
    '+237', '+238', '+239', '+240', '+241', '+242', '+243',
    '+244', '+245', '+246', '+246', '+247', '+248', '+249',
    '+250', '+251', '+252', '+253', '+254', '+255', '+255',
    '+256', '+257', '+258', '+260', '+261', '+262', '+262',
    '+263', '+264', '+265', '+266', '+267', '+268', '+269',
    '+290', '+291', '+297', '+298', '+299', '+350', '+351',
    '+352', '+353', '+354', '+355', '+356', '+357', '+358',
    '+359', '+370', '+371', '+372', '+373', '+374', '+375',
    '+376', '+377', '+378', '+379', '+380', '+381', '+382',
    '+383', '+385', '+386', '+387', '+389', '+420', '+421',
    '+423', '+500', '+500', '+501', '+502', '+503', '+504',
    '+505', '+506', '+507', '+508', '+509', '+590', '+590',
    '+590', '+591', '+592', '+593', '+594', '+595', '+596',
    '+596', '+597', '+598', '+670', '+672', '+672', '+673',
    '+674', '+675', '+676', '+677', '+678', '+679', '+680',
    '+681', '+682', '+683', '+685', '+686', '+687', '+688',
    '+689', '+690', '+691', '+692', '+800', '+808', '+850',
    '+852', '+853', '+855', '+856', '+870', '+878', '+880',
    '+881', '+886', '+960', '+961', '+962', '+963', '+964',
    '+965', '+966', '+967', '+968', '+970', '+971', '+972',
    '+973', '+974', '+975', '+976', '+977', '+992', '+993',
    '+994', '+995', '+996', '+998', '+1242', '+1246',
    '+1264', '+1268', '+1268', '+1284', '+1340', '+1345',
    '+1441', '+1473', '+1649', '+1664', '+1670', '+1671',
    '+1684', '+1721', '+1758', '+1767', '+1784', '+1808',
    '+1808', '+1849', '+1868', '+1869', '+1869', '+1876',
    '+1939', '+2908', '+4779', '+4779', '+5399', '+5993',
    '+5994', '+5997', '+5997', '+5999', '+8810', '+8813',
    '+8817', '+8818', '+35818', '+88213', '+88216',
    '+90392', '+99534', '+99544',
]
