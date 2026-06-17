# RXS_GROUP

> Contains items on an order set. For example: all the medications that are bee sting medicines.

**Description:** RxStation Group  
**Table type:** REFERENCE  
**Primary key:** `RXS_GROUP_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the group was created |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the person who created the group. |
| 4 | `GROUP_DESCRIPTION` | VARCHAR(100) | NOT NULL |  | The description or name of the group that is defined. |
| 5 | `RXS_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RXS_GROUP table. |
| 6 | `RXS_GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of group. Initially, the only type will be for an order set. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RXS_GROUP_ITEM_RELTN](RXS_GROUP_ITEM_RELTN.md) | `RXS_GROUP_ID` |
| [RXS_GROUP_LOCATION_RELTN](RXS_GROUP_LOCATION_RELTN.md) | `RXS_GROUP_ID` |

