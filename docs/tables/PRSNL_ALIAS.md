# PRSNL_ALIAS

> The person alias table contains information used identify a person (i.e., physician hospital number, UPIN number, etc.). There can be many rows in the personnel alias table that are related to a single row in the personnel table.

**Description:** Personnel Alias  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(200) |  |  | The alias is an identifier (I.e., doctor number, UPIN, etc.) for a personnel. The alias may be unique or non-unique depending on the type of alias. |
| 6 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | Alias pool code identifies a unique set or list of personnel identifiers (I.e., numbers). The alias pool code also determines the accept/display format for the unique set of identifiers. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CHECK_DIGIT` | DOUBLE |  |  | This is the value of the check digit calculated according to the check_digit_method_cd. If the check digit is stored as part of the alias number, which is typical, then the check digit field may be NULL. |
| 9 | `CHECK_DIGIT_METHOD_CD` | DOUBLE | NOT NULL |  | The check digit method code identifies a specific routine, using the alias field, to calculate a check digit. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 12 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 13 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 16 | `PRSNL_ALIAS_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person alias table. It is an internal system assigned number. |
| 17 | `PRSNL_ALIAS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Not Used |
| 18 | `PRSNL_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Personnel alias type code identifies a kind or type of alias (i.e., doctor number, UPIN, etc.). They have Cerner pre-defined meanings in the common data foundation table allowing HNA applications to look for a specific kind of alias. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

