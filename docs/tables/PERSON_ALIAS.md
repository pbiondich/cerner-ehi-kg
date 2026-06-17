# PERSON_ALIAS

> The person alias table contains information used to identify a person (i.e., medical record number, social security, etc.). There can be many rows in the person alias table that are related to a singlerow in the person table.

**Description:** Person Alias  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_ALIAS_ID`  
**Columns:** 33  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(200) | NOT NULL |  | The alias is an identifier (I.e., SSN, medical record number, etc.) for a person. The alias may be unique or non-unique depending on the type of alias. |
| 6 | `ALIAS_EXPIRY_DT_TM` | DATETIME |  |  | The date and time for which the alias is expired. |
| 7 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of person identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 8 | `ASSIGN_AUTHORITY_SYS_CD` | DOUBLE | NOT NULL |  | This field identifies whether the ESI Server received a Person_Alias that was configured for Hold. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CHECK_DIGIT` | DOUBLE |  |  | This is the value of the check digit calculated according to the check_digit_method_cd. If the check digit is stored as part of the alias number, which is typical, then the check digit field may be NULL. |
| 11 | `CHECK_DIGIT_METHOD_CD` | DOUBLE | NOT NULL |  | The check digit method code identifies a specific routine, using the alias field, to calculate a check digit. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 14 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 15 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `HEALTH_CARD_EXPIRY_DT_TM` | DATETIME |  |  | The date and time for which this health card becomes ineffective or expired. |
| 18 | `HEALTH_CARD_ISSUE_DT_TM` | DATETIME |  |  | The date and time for which this health card becomes effective or issued. |
| 19 | `HEALTH_CARD_PROVINCE` | CHAR(3) |  |  | Province in which the health card was issued with this alias was issued for a person. |
| 20 | `HEALTH_CARD_TYPE` | VARCHAR(32) |  |  | Type of health card which has a certain category or style. |
| 21 | `HEALTH_CARD_VER_CODE` | CHAR(3) |  |  | The latest recorded version of the health card with the associated alias value. |
| 22 | `PERSON_ALIAS_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person alias table. It is an internal system assigned number. |
| 23 | `PERSON_ALIAS_RECORD_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the current state of this person alias record. |
| 24 | `PERSON_ALIAS_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the current verification status of this person alias. |
| 25 | `PERSON_ALIAS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Person alias sub type code identifies a category within a particular person alias type code. For example, NAME is an alias type and MAIDEN is an alias sub type. |
| 26 | `PERSON_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Person alias type code identifies a kind or type of alias (i.e., SSN, MRN, Financial Number, Community MRN, etc.). They have Cerner pre-defined meanings in the common data foundation table allowing HNA applications to look for a specific kind of alias. |
| 27 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `VISIT_SEQ_NBR` | DOUBLE |  |  | Value used to track the number of encounters that have been created using the particular alias. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [MEDIA_MASTER](MEDIA_MASTER.md) | `PERSON_ALIAS_ID` |
| [PERSON_ORGAN_DONOR](PERSON_ORGAN_DONOR.md) | `INTL_ALIAS_ID` |
| [PERSON_ORGAN_DONOR](PERSON_ORGAN_DONOR.md) | `NMDP_ALIAS_ID` |
| [PERSON_ORGAN_DONOR](PERSON_ORGAN_DONOR.md) | `OPO_ALIAS_ID` |
| [PERSON_ORGAN_DONOR](PERSON_ORGAN_DONOR.md) | `UNOS_ALIAS_ID` |
| [PERSON_TRANSPLANT_CANDIDATE](PERSON_TRANSPLANT_CANDIDATE.md) | `HIC_ALIAS_ID` |
| [PERSON_TRANSPLANT_CANDIDATE](PERSON_TRANSPLANT_CANDIDATE.md) | `NMDP_ALIAS_ID` |
| [PERSON_TRANSPLANT_CANDIDATE](PERSON_TRANSPLANT_CANDIDATE.md) | `OPO_ALIAS_ID` |
| [PERSON_TRANSPLANT_CANDIDATE](PERSON_TRANSPLANT_CANDIDATE.md) | `PX_ALIAS_ID` |

