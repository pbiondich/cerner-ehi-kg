# AP_FT_TERM_PROC

> This reference table contains the report order catalog items that will cause a previously-initiated follow-up tracking event for a patient to be terminated. The termination action is triggered based on the verification of one of these reports.

**Description:** AP Followup Tracking Termination Procedure  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_TERMINATION_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the associated report order catalog item will cause an existing follow-up tracking event for a patient to be terminated when the report order catalog item is verified. |
| 2 | `AUTO_TERMINATION_REASON_CD` | DOUBLE | NOT NULL |  | If the termination report order catalog item is flagged to cause automatic (versus manual) termination, this field identifies the termination reason code value (from codeset 1313) to be assigned as the termination reason for the follow-up tracking event. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the order catalog report procedures associated with the follow-up tracking type. The verification of one of these reports causes any active follow-up tracking event for the patient to be evaluated for termination. |
| 4 | `FOLLOWUP_TRACKING_TYPE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the follow-up tracking type for which termination report order catalog items are assigned. This field contains the foreign key value used to join to follow-up type information stored on the AP_FT_TYPE reference table. |
| 5 | `LOOK_BACK_DAYS` | DOUBLE |  |  | This field contains the number of days that the system will look back to determine the presence of a termination report order catalog item. The report causing a follow-up event to be terminated may be verified before the follow-up event is initiated. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `FOLLOWUP_TRACKING_TYPE_CD` | [AP_FT_TYPE](AP_FT_TYPE.md) | `FOLLOWUP_TRACKING_TYPE_CD` |

