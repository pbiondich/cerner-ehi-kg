# TRANSFUSION

> Contains a record for every time a dispensed product is recorded as being transfused to the patientto whom it was dispensed.

**Description:** Transfusion  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BAG_RETURNED_IND` | DOUBLE |  |  | Indicates whether or not the empty bag was returned to the blood bank from the patient's location after it was transfused. |
| 6 | `CUR_TRANSFUSED_QTY` | DOUBLE |  |  | This column applies only to derivative products. It is the quantity of the derivative batch that is currently in a transfused state. |
| 7 | `ORIG_TRANSFUSED_QTY` | DOUBLE |  |  | This column applies only to derivative products. It is the quantity of the derivative batch that was originally recorded as being in a transfused state for the patient. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 9 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to this table, as well as the PRODUCT_EVENT table. An internal system-assigned number that ensure the uniqueness of each row. For every row on this table, there is a corresponding row on the PRODUCT_EVENT table with the same Product_Event_ID. |
| 10 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it represents the product that was transfused to the patient. |
| 11 | `TAG_RETURNED_IND` | DOUBLE |  |  | Indicates whether the tag attached to the bag dispensed was returned to the blood bank following the transfusion. |
| 12 | `TRANSFUSED_INTL_UNITS` | DOUBLE |  |  | This column applies only to derivative products. It is the number of international units that was transfused to the patient. |
| 13 | `TRANSFUSED_VOL` | DOUBLE |  |  | The volume of the product that was actually infused into the patient. This amount may not be the entire volume that was in the bag. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

