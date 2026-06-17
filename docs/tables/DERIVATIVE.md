# DERIVATIVE

> Attributes that are specific to a derivative (as opposed to a blood product).

**Description:** Derivative  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CUR_AVAIL_QTY` | DOUBLE |  |  | The current quantity available for use and not already designated for other uses (ex. 80 vials of Factor VIII, 5 bottles of Rhogam, etc.) |
| 6 | `CUR_INTL_UNITS` | DOUBLE |  |  | The number of international units currently available for use. |
| 7 | `ITEM_UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | The unit of measure for each item within the derivative batch (ex. "VL" for vial) |
| 8 | `ITEM_VOLUME` | DOUBLE |  |  | The volume of each item within the derivative batch. |
| 9 | `MANUFACTURER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the organization which manufactured this derivative batch. |
| 10 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The exact type of derivative product in this batch (ex. "Rhogam", "Factor VIII"). |
| 11 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The Product ID from the PRODUCT table, which makes this table unique. |
| 12 | `UNITS_PER_VIAL` | DOUBLE |  |  | Number of international units per vial |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MANUFACTURER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

