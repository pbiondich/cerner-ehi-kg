# CHARGE_BATCH_DETAIL_CODE

> Stores bill codes associated to each charge detail.

**Description:** Charge Batch Detail Code  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHARGE_BATCH_DETAIL_CODE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a bill code that is associated to a charge detail. |
| 3 | `CHARGE_BATCH_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related charge batch detail record. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the id of the related parent entity. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The table that is the source for the id value in the parent_entity_id field. |
| 6 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | The priority of the bill code. |
| 7 | `TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of bill code row. |
| 8 | `TYPE_IDENT` | VARCHAR(50) | NOT NULL |  | Contains the bill code value input by the user. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_BATCH_DETAIL_ID` | [CHARGE_BATCH_DETAIL](CHARGE_BATCH_DETAIL.md) | `CHARGE_BATCH_DETAIL_ID` |

