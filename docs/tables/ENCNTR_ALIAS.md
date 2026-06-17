# ENCNTR_ALIAS

> The encounter alias table contains information used identify an encounter (i.e., financial number, requisition number, etc.). There can be many rows in the encounter alias table that are related to a single row in the encounter table.

**Description:** Encounter Alias  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_ALIAS_ID`  
**Columns:** 24  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(200) |  |  | The alias is an identifier (I.e., financial number) for an encounter. The alias may be unique or non-unique depending on the type of alias. |
| 6 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of encounter identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 7 | `ASSIGN_AUTHORITY_SYS_CD` | DOUBLE |  |  | This field identifies whether the ESI Server received a Person_Alias that was configured for Hold. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CHECK_DIGIT` | DOUBLE |  |  | This is the value of the check digit calculated according to the check_digit_method_cd. If the check digit is stored as part of the alias number, which is typical, then the check digit field may be NULL. |
| 10 | `CHECK_DIGIT_METHOD_CD` | DOUBLE | NOT NULL |  | The check digit method code identifies a specific routine, using the alias field, to calculate a check digit. |
| 11 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 12 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 13 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 14 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 15 | `ENCNTR_ALIAS_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter alias table. It is an internal system assigned number. |
| 16 | `ENCNTR_ALIAS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | NOT USED |
| 17 | `ENCNTR_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Encounter alias type code identifies a kind or type of alias (i.e., Financial Number, Encounter Number, etc.). They are Cerner pre-defined meanings in the common data foundation table allowing HNA applications to look for a specific kind of alias. |
| 18 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 19 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ENCNTR_ALIAS_HIST](ENCNTR_ALIAS_HIST.md) | `ENCNTR_ALIAS_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `FINNBR_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `MEDREC_NBR_ID` |

