# PHONE_HIST

> Tracks modifications to history elements for a given phone table.

**Description:** PHONE HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 39

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CALL_INSTRUCTION` | VARCHAR(300) |  |  | This is a text field to be used to indicate any specific protocol or instructions to be followed when calling this phone number |
| 7 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 8 | `CONTACT` | VARCHAR(100) |  |  | The primary person or contacted for this phone number. |
| 9 | `CONTACT_METHOD_CD` | DOUBLE | NOT NULL |  | The intended method of contact to be used for phone entry. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 12 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 13 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 14 | `DESCRIPTION` | VARCHAR(100) |  |  | This is a text description for identifying who or where this phone number is associated with. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `EXTENSION` | VARCHAR(100) |  |  | This is the local phone extension of a person or place as in a business office environment. |
| 17 | `OPERATION_HOURS` | VARCHAR(255) |  |  | Free-text entry detailing the days and hours this phone number is valid |
| 18 | `PAGING_CODE` | VARCHAR(100) |  |  | This is the specific pager number to be used after dialing a main or central pager number. |
| 19 | `PARENT_BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | This is the historical record of column BEG_EFFECTIVE_DT_TM in table PHONE. |
| 20 | `PARENT_END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | This is the historical record of column END_EFFECTIVE_DT_TM in table PHONE. |
| 21 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the phone row is related (i.e., person_id, organization_id, etc.) |
| 22 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | The upper case name of the table to which this phone row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 23 | `PHONE_FORMAT_CD` | DOUBLE | NOT NULL |  | Phone Number Format Code Value (future use) |
| 24 | `PHONE_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the phone_hist table. It is an internal system assigned number. |
| 25 | `PHONE_ID` | DOUBLE | NOT NULL | FK→ | Phone ID is the primary unique identification number of the phone table. It is an internal system assigned sequence number. |
| 26 | `PHONE_NUM` | VARCHAR(100) |  |  | This is the actual phone number. |
| 27 | `PHONE_NUM_KEY` | VARCHAR(100) |  |  | The phone_num attribute converted to a string with spaces and special characters removed. |
| 28 | `PHONE_TYPE_CD` | DOUBLE | NOT NULL |  | The phone type is the code set value which identifies the type of phone for the phone row (i.e., home, business, fax, etc.) |
| 29 | `PHONE_TYPE_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the priority or precedence that one phone row has over another when both phone rows contain the same parent_entity_name, parent_entity_id, and phone_type_cd with the same meaning. |
| 30 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 31 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support the uk's pds allocated object identifier. Used to help keep the uk master in sync with millennnium. |
| 32 | `TEXTING_PERMISSION_CD` | DOUBLE | NOT NULL |  | Denotes if the owner of the phone has granted permission to be contacted by text message. |
| 33 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 34 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 35 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

