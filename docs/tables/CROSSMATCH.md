# CROSSMATCH

> A record of every time a product was updated to a crossmatch status for a patient, in result entry.

**Description:** Crossmatch  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BB_ID_NBR` | VARCHAR(20) |  |  | The patient's Blood Bank ID number, usually a wristband number or Hollister-Fenwal number, entered at the time of crossmatch. |
| 6 | `CROSSMATCH_EXP_DT_TM` | DATETIME |  |  | The date and time when this crossmatch will expire. |
| 7 | `CROSSMATCH_QTY` | DOUBLE |  |  | This column only applies to derivative types of products. It contains the quantity of the derivative that was crossmatched. ***NOT USED AT THIS TIME |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 9 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the product_event table. It is an internal system-assigned number. |
| 10 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the product table. It is an internal system-assigned number. On this table, it denotes the product crossmatched. |
| 11 | `REINSTATE_REASON_CD` | DOUBLE | NOT NULL |  | If this crossmatch was released and then later reinstated, it is the reason for that reinstatement. |
| 12 | `RELEASE_DT_TM` | DATETIME |  |  | If this crossmatch was released, it denotes the date and time it was released. |
| 13 | `RELEASE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that released this crossmatch. |
| 14 | `RELEASE_QTY` | DOUBLE |  |  | This column only applies to derivative types of products. It contains the quantity of the derivative that was released from being crossmatched. ***NOT USED AT THIS TIME |
| 15 | `RELEASE_REASON_CD` | DOUBLE | NOT NULL |  | The reason this crossmatch was released from the patient. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `XM_REASON_CD` | DOUBLE | NOT NULL |  | The reason this product was crossmatched to this patient (ex. "Surgery", etc.) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `RELEASE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

