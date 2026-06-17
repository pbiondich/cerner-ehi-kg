# PULL_TRANS_REQ

> The Pull_Trans_Req table contains information specific to transfer and request pull lists.

**Description:** Transfer/Request Pull Lists  
**Table type:** ACTIVITY  
**Primary key:** `PULL_LIST_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BORROWING_ENTITY_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** The Borrowing_Entity_Id contains the primary key of the table that contains the borrower. This, along with the borrowing_entity_name, identifies the borrower whose request generated the request pull list. |
| 2 | `BORROWING_ENTITY_NAME` | VARCHAR(32) |  |  | *** OBSOLETE *** The Borrowing_Entity_Name contains the name of the table that contains the borrower. This, along with the borrowing_entity_id, identifies the borrower whose request generated the request pull list. |
| 3 | `FROM_LIB_CD` | DOUBLE | NOT NULL | FK→ | The From_Lib_Cd identifies the library that folders will be pulled from as a part of a transfer. |
| 4 | `PULL_LIST_ID` | DOUBLE | NOT NULL | PK FK→ | The Pull_List_Id is a foreign key to the Pull_List table. It identifies which pull list this is related to. |
| 5 | `TO_LIB_CD` | DOUBLE | NOT NULL | FK→ | The To_Lib_Cd identifies the library that folders will be moving to as a part of a transfer. |
| 6 | `TRANS_RULE_ID` | DOUBLE | NOT NULL | FK→ | The trans_rule_id serves as a foreign key to the rad_fold_trans_rule table. It uniquely identifies the transfer rule that was used. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FROM_LIB_CD` | [TRACK_PT_LIBRARY](TRACK_PT_LIBRARY.md) | `SERVICE_RESOURCE_CD` |
| `PULL_LIST_ID` | [PULL_LIST](PULL_LIST.md) | `PULL_LIST_ID` |
| `TO_LIB_CD` | [TRACK_PT_LIBRARY](TRACK_PT_LIBRARY.md) | `SERVICE_RESOURCE_CD` |
| `TRANS_RULE_ID` | [RAD_FOLD_TRANS_RULE](RAD_FOLD_TRANS_RULE.md) | `TRANS_RULE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PULL_FOLDERS](PULL_FOLDERS.md) | `PULL_LIST_ID` |

