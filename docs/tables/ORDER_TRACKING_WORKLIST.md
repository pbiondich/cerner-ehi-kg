# ORDER_TRACKING_WORKLIST

> Tracked orders for physicians.

**Description:** Order Tracking Worklist  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Sub activity type order. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Activity type of the order. |
| 3 | `CATALOG_CD` | DOUBLE |  | FK→ | The catalog code associated to the order. |
| 4 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog type of the order. |
| 5 | `DEPT_STATUS_CD` | DOUBLE | NOT NULL |  | The departmental status of the order |
| 6 | `EFFECTIVE_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The effective encounter of the order. |
| 7 | `END_DUE_DT_TM` | DATETIME |  |  | End due date and time of the order. |
| 8 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The unique order ID |
| 9 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the ordering provider. |
| 10 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the order. |
| 11 | `ORDER_TRACKING_WORKLIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDERS_TRACKING_WORKLIST table. |
| 12 | `ORIGINATING_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Originating nurse unit from where the order was placed. |
| 13 | `ORIG_ORD_DT_TM` | DATETIME |  |  | Originally ordered date and time of the order. |
| 14 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | The patient ID for who the order was created. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `EFFECTIVE_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

