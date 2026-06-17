# MM_ITEM_ORG_COST_HIST

> Stores history of costs that have been manually updated in the ITEM_LOCATION_COST table.

**Description:** Item Organization Cost History  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COST_TYPE_CD` | DOUBLE | NOT NULL |  | The cost type code allows differentiation between average cost, current cost, last cost, etc. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time that this row was created. |
| 3 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that had a cost changed. |
| 4 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that last updated this row. |
| 5 | `MM_ITEM_ORG_COST_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_ITEM_ORG_COST_HIST table. |
| 6 | `ORG_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location code for the organization that had a cost change. |
| 7 | `ORIG_ORG_COST_AMT` | DOUBLE | NOT NULL |  | The cost before the change. |
| 8 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The base package type for the item. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_MANUAL_ORG_COST_AMT` | DOUBLE | NOT NULL |  | The changed cost amount. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORG_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

