# PHONE

> The phone table contains all phone numbers in the system. A row in the phone table is associated with a row in another table (i.e., person, organization, location, etc.).

**Description:** Phone  
**Table type:** ACTIVITY  
**Primary key:** `PHONE_ID`  
**Columns:** 38  
**Referenced by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_EFFECTIVE_MM_DD` | DOUBLE |  |  | The numeric representation of the month and day of the month for which this row becomes effective within the current year. |
| 7 | `CALL_INSTRUCTION` | VARCHAR(300) |  |  | This is a text field to be used to indicate any specific protocol or instructions to be followed when calling this phone number |
| 8 | `CONTACT` | VARCHAR(100) |  |  | The primary person or contacted for this phone number. |
| 9 | `CONTACT_METHOD_CD` | DOUBLE | NOT NULL |  | The intended method of contact to be used for phone entry. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 12 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 13 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 14 | `DESCRIPTION` | VARCHAR(100) |  |  | This is a text description for identifying who or where this phone number is associated with. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `END_EFFECTIVE_MM_DD` | DOUBLE |  |  | The numeric representation of the month and day of the month for which this row is no longer effective within the current year. |
| 17 | `EXTENSION` | VARCHAR(100) |  |  | This is the local phone extension of a person or place as in a business office environment. |
| 18 | `LONG_TEXT_ID` | DOUBLE |  |  | Foreign Key to the LONG_TEXT table to provide phone level comments |
| 19 | `MODEM_CAPABILITY_CD` | DOUBLE | NOT NULL |  | Code value for Modem Capability. (future use) |
| 20 | `OPERATION_HOURS` | VARCHAR(255) |  |  | free text entry detailing the days and hours this phone number is valid |
| 21 | `PAGING_CODE` | VARCHAR(100) |  |  | This is the specific pager number to be used after dialing a main or central pager number. |
| 22 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the phone row is related (i.e., person_id, organization_id, etc.) |
| 23 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this phone row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 24 | `PHONE_FORMAT_CD` | DOUBLE | NOT NULL |  | Phone Number Format Code Value (future use) |
| 25 | `PHONE_ID` | DOUBLE | NOT NULL | PK | Phone ID is the primary unique identification number of the phone table. It is an internal system assigned sequence number. |
| 26 | `PHONE_NUM` | VARCHAR(100) |  |  | This is the actual phone number. |
| 27 | `PHONE_NUM_KEY` | VARCHAR(100) |  |  | Phone_num attribute converted to a string with SPACES and special characters removed. |
| 28 | `PHONE_NUM_KEY_A_NLS` | VARCHAR(400) |  |  | PHONE_NUM_KEY_A_NLS column |
| 29 | `PHONE_NUM_KEY_NLS` | VARCHAR(202) |  |  | Stores the corresponding non-English character set values for attribute Phone_Num_Key |
| 30 | `PHONE_TYPE_CD` | DOUBLE | NOT NULL |  | The phone type is the code set value which identifies the type of phone for the phone row (i.e., home, business, fax, etc.) |
| 31 | `PHONE_TYPE_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the priority or precedence that one phone row has over another when both phone rows contain the same parent_entity_name, parent_entity_id, and phone_type_cd with the same meaning. |
| 32 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support he UK's PDS Allocated Object Identifier. Used to help keep the UK master database in sync with Millennium. |
| 33 | `TEXTING_PERMISSION_CD` | DOUBLE | NOT NULL |  | Denotes if the owner of the phone has granted permission to be contacted by text message. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (18)

| From table | Column |
|------------|--------|
| [CSM_LST_CONTACT](CSM_LST_CONTACT.md) | `PHONE_ID` |
| [CSM_REQUESTS](CSM_REQUESTS.md) | `PHONE_ID` |
| [CSM_REQUESTS](CSM_REQUESTS.md) | `SELECTED_PHONE_ID` |
| [CSM_REQUESTS_ARCHIVE](CSM_REQUESTS_ARCHIVE.md) | `PHONE_ID` |
| [MRU_LOOKUP_FOLLOWUP](MRU_LOOKUP_FOLLOWUP.md) | `PHONE_ID` |
| [PFT_AP_REFUND](PFT_AP_REFUND.md) | `PHONE_ID` |
| [PHONE_HIST](PHONE_HIST.md) | `PHONE_ID` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_PER_BUS_PHONE_ID` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `O_PER_HOME_PHONE_ID` |
| [REFERRAL_CONTACT](REFERRAL_CONTACT.md) | `PHONE_ID` |
| [REQUESTER](REQUESTER.md) | `BILL_TO_FAX_ID` |
| [REQUESTER](REQUESTER.md) | `BILL_TO_PHONE_ID` |
| [REQUESTER](REQUESTER.md) | `MAIL_TO_FAX_ID` |
| [REQUESTER](REQUESTER.md) | `MAIL_TO_PHONE_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `BILL_TO_FAX_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `BILL_TO_PHONE_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `MAIL_TO_FAX_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `MAIL_TO_PHONE_ID` |

