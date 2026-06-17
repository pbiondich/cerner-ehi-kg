# CT_USER_PREFERENCE

> Stores the clinical trial filter preferences for each user

**Description:** Clinical Trials - User Preferences  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CT_FACILITY_CD_GROUP_ID` | DOUBLE | NOT NULL | FK→ | FK value from a row in the CT_FACILITY_CD_GROUP table wihich helps identify a group of facilities |
| 6 | `CT_USER_PREFERENCE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `FUNCTIONALITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of functionality for which the filter preferences are stored |
| 8 | `PREFERENCE_STATUS_FLAG` | DOUBLE | NOT NULL |  | A status which indicates whether the preference was shared by other user or saved personally |
| 9 | `PREFERENCE_TEXT` | LONGTEXT |  |  | A large object block which contains the user preference data in text form. |
| 10 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | FK value for a row in the PROT_MASTER table |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unqiue Id of prsnl whose filter preferences in powertrials application needs to be stored |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_FACILITY_CD_GROUP_ID` | [CT_FACILITY_CD_GROUP](CT_FACILITY_CD_GROUP.md) | `CT_FACILITY_CD_GROUP_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

