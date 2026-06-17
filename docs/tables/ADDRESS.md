# ADDRESS

> The address table contains all addresses. An address table row is associated with a row in another table (i.e., person). Each address row is identified by the name of the table it is related to & the related table's primary row identifier.

**Description:** Address  
**Table type:** ACTIVITY  
**Primary key:** `ADDRESS_ID`  
**Columns:** 53  
**Referenced by:** 15 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADDRESS_FORMAT_CD` | DOUBLE | NOT NULL |  | Address format code identifies the format to apply to the given address. (Future Use) |
| 6 | `ADDRESS_ID` | DOUBLE | NOT NULL | PK | The address ID is the primary key of the address table. |
| 7 | `ADDRESS_INFO_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the address. An example would be 'Incorrect Address'. |
| 8 | `ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | The address type is the code set value which identifies the type of address for the address row (i.e., home, business, etc.) |
| 9 | `ADDRESS_TYPE_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the priority or precedence that one address row has over another when both address rows contain the same parent_entity_name, parent_entity_id, and address_type_cd with the same meaning. |
| 10 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 11 | `BEG_EFFECTIVE_MM_DD` | DOUBLE |  |  | The numeric representation of the month and day of the month for which this row becomes effective within the current year. |
| 12 | `CITY` | VARCHAR(100) |  |  | The city field is the text name of the city associated with the address row. |
| 13 | `CITY_CD` | DOUBLE | NOT NULL |  | The city code is the code set value which identifies the city for the address row. |
| 14 | `COMMENT_TXT` | VARCHAR(200) |  |  | Comment giving additional information about the address. |
| 15 | `CONTACT_NAME` | VARCHAR(200) |  |  | The primary person or contact for this address. |
| 16 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 17 | `COUNTRY` | VARCHAR(100) |  |  | The country field is the text name of the country associated with the address row. |
| 18 | `COUNTRY_CD` | DOUBLE | NOT NULL |  | The country code is the code set value which identifies the country for the address row. |
| 19 | `COUNTY` | VARCHAR(100) |  |  | The county field is the text name of the county associated with the address row. |
| 20 | `COUNTY_CD` | DOUBLE | NOT NULL |  | The county code is the code set value which identifies the county for the address row. |
| 21 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 22 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 23 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 24 | `DISTRICT_HEALTH_CD` | DOUBLE | NOT NULL |  | This will hold the code_value of the District Health Authority. |
| 25 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 26 | `END_EFFECTIVE_MM_DD` | DOUBLE |  |  | The numeric representation of the month and day of the month for which this row is no longer effective within the current year. |
| 27 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from LONG_TEXT table. Ties free text comments to an address. |
| 28 | `MAIL_STOP` | VARCHAR(100) |  |  | Currently used internally by Cerner only. Identifies a Cerner organization mail stop number used to route inter-office mail. |
| 29 | `OPERATION_HOURS` | VARCHAR(255) |  |  | free text entry specifying the days and hours that this address is valid |
| 30 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the address row is related (i.e., person_id, organization_id, etc.) |
| 31 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this address row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 32 | `POSTAL_BARCODE_INFO` | VARCHAR(100) |  |  | This contains Postal Barcode Information of the address. (future use) |
| 33 | `POSTAL_IDENTIFIER` | VARCHAR(100) |  |  | A code that is used to assist with finding or navigating to a specific location or delivery point. In some countries, this may provide better resolution than the standard postal address. |
| 34 | `POSTAL_IDENTIFIER_KEY` | VARCHAR(100) |  |  | Stores a version of column Postal Identifier with all the spaces removed and in upper case. Used as a consistent key field for column Postal Identifier. |
| 35 | `PRIMARY_CARE_CD` | DOUBLE | NOT NULL |  | This will hold the code_value of the Primary Care Trust. |
| 36 | `RESIDENCE_CD` | DOUBLE | NOT NULL |  | The residence code is the code set value which identifies a geographic area for user defined purposes. In Canada, the residence code is used for billing and statistical purposes between the provinces. |
| 37 | `RESIDENCE_TYPE_CD` | DOUBLE | NOT NULL |  | The residence type code is a code set value which describes key physical characteristics about the housing or building associated with the address. (I.e., apartment, house, etc.) |
| 38 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support he UK's PDS Allocated Object Identifier. Used to help keep the UK master database in sync with Millennium. |
| 39 | `STATE` | VARCHAR(100) |  |  | The state field is the text name of the state or province associated with the address row. |
| 40 | `STATE_CD` | DOUBLE | NOT NULL |  | The state code is the code set value which identifies the state or province for the address row. |
| 41 | `STREET_ADDR` | VARCHAR(100) |  |  | This is the first line of the street address. |
| 42 | `STREET_ADDR2` | VARCHAR(100) |  |  | This is the second line of the street address. |
| 43 | `STREET_ADDR3` | VARCHAR(100) |  |  | This is the third line of the street address. The third line of the street address will generally only be used for international addresses. |
| 44 | `STREET_ADDR4` | VARCHAR(100) |  |  | This is the fourth line of the street address. The fourth line of the street address will generally only be used for international addresses. |
| 45 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `VALIDATION_EXPIRE_DT_TM` | DATETIME |  |  | The time in which the address validation expires. |
| 51 | `ZIPCODE` | VARCHAR(25) |  |  | This field contains the postal code for the street address in the address row. |
| 52 | `ZIPCODE_KEY` | VARCHAR(25) |  |  | Zipcode key field converted to nls format for internationalization and search requirements |
| 53 | `ZIP_CODE_GROUP_CD` | DOUBLE | NOT NULL |  | This contains the code set value for a zip code group. (future use) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (15)

| From table | Column |
|------------|--------|
| [ADDRESS_HIST](ADDRESS_HIST.md) | `ADDRESS_ID` |
| [INVOICE](INVOICE.md) | `REMIT_ADDRESS_ID` |
| [MRU_LOOKUP_FOLLOWUP](MRU_LOOKUP_FOLLOWUP.md) | `ADDRESS_ID` |
| [PFT_AP_REFUND](PFT_AP_REFUND.md) | `ADDRESS_ID` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_PER_BUS_ADDRESS_ID` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_PER_HOME_ADDRESS_ID` |
| [PRODUCT_DEFAULT_ADDRESS](PRODUCT_DEFAULT_ADDRESS.md) | `ADDRESS_ID` |
| [PURCHASE_ORDER](PURCHASE_ORDER.md) | `BILL_TO_ADDRESS_ID` |
| [PURCHASE_ORDER](PURCHASE_ORDER.md) | `SHIP_TO_ADDRESS_ID` |
| [PURCHASE_ORDER](PURCHASE_ORDER.md) | `VENDOR_ADDRESS_ID` |
| [REQUESTER](REQUESTER.md) | `BILL_TO_ADDRESS_ID` |
| [REQUESTER](REQUESTER.md) | `MAIL_TO_ADDRESS_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `BILL_TO_ADDRESS_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `MAIL_TO_ADDRESS_ID` |
| [SI_UNMTCHD_PRSN_QUE](SI_UNMTCHD_PRSN_QUE.md) | `ADDRESS_ID` |

