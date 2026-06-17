# UCM_DSR_VARIANT

> Stores variant results for an order.

**Description:** Unified Case Manager - Document Sequencing Results Variant  
**Table type:** ACTIVITY  
**Primary key:** `UCM_DSR_VARIANT_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order (i.e., panel) used to obtain this variant result. |
| 6 | `PREV_UCM_DSR_VARIANT_ID` | DOUBLE | NOT NULL |  | Used to track versions of the variant information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 7 | `REPORTABLE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the variant is capable of being pulled into Document Case Report. |
| 8 | `UCM_DSR_VARIANT_ID` | DOUBLE | NOT NULL | PK | Uniquely stores variant results for an order. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VARIANT_NAME` | VARCHAR(250) |  |  | The name of the variant. |
| 15 | `VARIANT_SEQ` | DOUBLE | NOT NULL |  | The sequence of rows in the order the variants were created or imported. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UCM_DSR_VARIANT_INFO](UCM_DSR_VARIANT_INFO.md) | `UCM_DSR_VARIANT_ID` |

