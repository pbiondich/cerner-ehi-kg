# SI_CODE_SET_INTERFACE_HIST

> This table store historical information created by modifications to the CODE_SET_INTERFACE table.

**Description:** System Integration Code Set Interface History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | The Alias Type Meaning of the modified record from the Code Set Interface table. |
| 6 | `CODE_SET` | DOUBLE | NOT NULL |  | The Code Set of the modified record from the Code Set Interface table. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DEFAULT_ALIAS` | VARCHAR(255) | NOT NULL |  | The Default Alias of the modified record from the Code Set Interface table. |
| 9 | `DEFAULT_CD` | DOUBLE | NOT NULL |  | The Default Code of the modified record from the Code Set Interface table. |
| 10 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made new modification on the code_set_interface table |
| 11 | `ORIG_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl ID of the user who made original record on the code_set_interface table |
| 12 | `PARENT_ACTIVE_IND` | DOUBLE | NOT NULL |  | Active_Ind of the modified record from the code_set_interface table |
| 13 | `PROCESS_CD` | DOUBLE | NOT NULL |  | The Process Code of the modified record from the Code Set Interface table. |
| 14 | `REC_BEG_EFF_DT_TM` | DATETIME |  |  | Copy of the Beg_Eff_Dt_TM from the code_set_interface Table |
| 15 | `SI_CODE_SET_INTERFACE_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 16 | `SYS_DIRECTION_CD` | DOUBLE | NOT NULL |  | The System Direction code of the modified record from the Code Set Interface table. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

