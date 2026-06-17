# OMF_COST

> Stores the standard cost information.

**Description:** OMF COST  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BEG_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `BILL_ITEM_ID` | DOUBLE | NOT NULL |  | The unique identifier assigned to a bill item OR the code value for a specific cost basis. |
| 5 | `COST_BASIS_TYPE_CD` | DOUBLE | NOT NULL |  | Describes the cost basis for the standard cost (i.e. bill item, revenue code, revenue category, etc.). |
| 6 | `DIRECT_FIX_COST` | DOUBLE |  |  | The direct fixed cost associated to the bill item. |
| 7 | `DIRECT_VAR_COST` | DOUBLE |  |  | The direct variable cost associated with the bill item. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `END_EFFECTIVE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `INDIRECT_FIX_COST` | DOUBLE |  |  | The indirect fix cost associated with the bill_item |
| 11 | `INDIRECT_VAR_COST` | DOUBLE |  |  | The indirect variable cost associated with the bill item. |
| 12 | `OMF_COST_ID` | DOUBLE | NOT NULL |  | The unique identifier for a row on the OMF_COST table |
| 13 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the organization for which the costs are to be applied. |
| 14 | `STD_IND` | DOUBLE |  |  | Indicates whether the row is a standard cost or an actual cost for a bill item (1=standard cost; 0=actual cost). |
| 15 | `TOTAL_COST` | DOUBLE |  |  | Total cost is used when sending totals only across the interface. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

