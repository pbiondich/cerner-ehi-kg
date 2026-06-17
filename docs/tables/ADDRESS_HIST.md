# ADDRESS_HIST

> Tracks modifications to history elements for a given address table.

**Description:** ADDRESS HISTORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 50

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADDRESS_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the address_hist table. It is an internal system assigned number. |
| 6 | `ADDRESS_ID` | DOUBLE | NOT NULL | FK→ | The ADDRESS_ID value inherited from the ADDRESS table. |
| 7 | `ADDRESS_INFO_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the address. An example would be 'Incorrect Address'. |
| 8 | `ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | The address type is the code set value which identifies the type of address for the address row (i.e., home, business, etc.) |
| 9 | `ADDRESS_TYPE_SEQ` | DOUBLE |  |  | This is the numeric sequence that determines the priority or precedence that one address row has over another when both address rows contain the same parent_entity_name, parent_entity_id and address_type_cd with the same meaning. |
| 10 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 11 | `CITY` | VARCHAR(100) |  |  | The city field is the text name of the city associated with the address row. |
| 12 | `CITY_CD` | DOUBLE | NOT NULL |  | The city code is the code set value which identifies the city for the address row. |
| 13 | `COMMENT_TXT` | VARCHAR(200) |  |  | Comment giving additional information about the address. |
| 14 | `CONTACT_NAME` | VARCHAR(200) |  |  | The primary person or contact for this address. |
| 15 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 16 | `COUNTRY` | VARCHAR(100) |  |  | The country field is the text name of the country associated with the address row. |
| 17 | `COUNTRY_CD` | DOUBLE | NOT NULL |  | The country code is the code set value which identifies the country for the address row. |
| 18 | `COUNTY` | VARCHAR(100) |  |  | The county field is the text name of the county associated with the address row. |
| 19 | `COUNTY_CD` | DOUBLE | NOT NULL |  | The county code is the code set value which identifies the county for the address row. |
| 20 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 21 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 22 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 23 | `MAIL_STOP` | VARCHAR(100) |  |  | Currently used internally by Cerner only. Identifies a Cerner organization mail stop number used to route inter-office mail. |
| 24 | `OPERATION_HOURS` | VARCHAR(255) |  |  | Free-text entry specifying the days and hours that this address is valid |
| 25 | `PARENT_BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | This is the historical record of column BEG_EFFECTIVE_DT_TM in table ADDRESS. |
| 26 | `PARENT_END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | This is the historical record of column END_EFFECTIVE_DT_TM in table ADDRESS. |
| 27 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the address row is related (i.e., person_id, organization_id, etc.) |
| 28 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The upper case name of the table to which this address row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 29 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 30 | `POSTAL_IDENTIFIER` | VARCHAR(100) |  |  | A code that is used to assist with finding or navigating to a specific location or delivery point. In some countries, this may provide better resolution than the standard postal address. |
| 31 | `POSTAL_IDENTIFIER_KEY` | VARCHAR(100) |  |  | Stores a version of column postal identifier with all the spaces removed and in upper case. Used as a consistent key field for column postal identifier. |
| 32 | `RESIDENCE_CD` | DOUBLE | NOT NULL |  | The residence code is the code set value which identifies a geographic area for user defined purposes. In Canada, the residence code is used for billing and statistical purposes between the provinces. |
| 33 | `RESIDENCE_TYPE_CD` | DOUBLE | NOT NULL |  | The residence type code is a code set value which describes key physical characteristics about the housing or building associated with the address. (I.e., apartment, house, etc.) |
| 34 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support the uk's pds allocated object identifier. Used to help keep the uk master database in sync with Millennium. |
| 35 | `STATE` | VARCHAR(100) |  |  | The state field is the text name of the state or province associated with the address row. |
| 36 | `STATE_CD` | DOUBLE | NOT NULL |  | The state code is the code set value which identifies the state or province for the address row. |
| 37 | `STREET_ADDR` | VARCHAR(100) |  |  | This is the first line of the street address. |
| 38 | `STREET_ADDR2` | VARCHAR(100) |  |  | This is the second line of the street address. |
| 39 | `STREET_ADDR3` | VARCHAR(100) |  |  | This is the third line of the street address. The third line of the street address will generally only be used for international addresses. |
| 40 | `STREET_ADDR4` | VARCHAR(100) |  |  | This is the fourth line of the street address. The fourth line of the street address will generally only be used for international addresses. |
| 41 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 42 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `VALIDATION_EXPIRE_DT_TM` | DATETIME |  |  | The time in which the address validation expires. |
| 49 | `ZIPCODE` | VARCHAR(25) |  |  | This field contains the postal code for the street address in the address row. |
| 50 | `ZIPCODE_KEY` | VARCHAR(25) |  |  | alpha numeric zip code in NLS format. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDRESS_ID` | [ADDRESS](ADDRESS.md) | `ADDRESS_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

