# EKS_MODULESTORAGE

> The module storage table contains the encoded defintion of the module including the templates used, and their conjunctive and disjunctive relationships.

**Description:** module definition storage table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_SEQ` | DOUBLE | NOT NULL |  | The eks_module table's num_storage field describes the count of module storage records required to describe the module details. The DATA_SEQ field is the offset of a module storage record within the set used to describe the module. |
| 2 | `DATA_TYPE` | DOUBLE | NOT NULL |  | Type of the data held within this record. The types basically denote which section of the module is being stored in this record (EVOKE, DATA,LOGIC,ACTION). |
| 3 | `EKM_INFO` | LONGTEXT |  |  | The text of the module containing the templates and parameters and their conjunctive/disjunctive relationships. |
| 4 | `MODULE_NAME` | CHAR(30) | NOT NULL |  | The name of the module this record is associated with. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VERSION` | CHAR(10) | NOT NULL |  | The version of the module that this record is associated with. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

