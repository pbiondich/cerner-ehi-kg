# SA_REF_DILUENT

> Stores reference data for diluents

**Description:** SA_REF_DILUENT  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_DILUENT_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that identifies the diluent item, FK from item_master |
| 6 | `SA_REF_DILUENT_ID` | DOUBLE | NOT NULL | PK | Unique value to the diluent record. Primary Key. |
| 7 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of item for display. Applys to all ACTIVE rows in the table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `SA_REF_DILUENT_ID` |
| [SA_REF_EXCLUDE_DILUENT](SA_REF_EXCLUDE_DILUENT.md) | `SA_REF_DILUENT_ID` |

