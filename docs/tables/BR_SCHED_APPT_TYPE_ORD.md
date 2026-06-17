# BR_SCHED_APPT_TYPE_ORD

> Hold orders for appointment types that are orders based

**Description:** Bedrock Scheduling Appointment Type Order  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Activity subtype of the default orders the department type can be scheduled for |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Activity type of the default orders the department type can be scheduled for |
| 3 | `APPT_TYPE_ID` | DOUBLE | NOT NULL |  | identifier of the appointment type |
| 4 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 5 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Catalog type of the default orders the department type can be scheduled for |
| 6 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Concept_cki to link the order to order_catalog table |
| 7 | `DURATION` | DOUBLE |  |  | number to define the duration on sch_order_duration when the appointment type/order relationship is created |
| 8 | `PRIMARY_MNEMONIC` | VARCHAR(100) |  |  | Description of the order |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

