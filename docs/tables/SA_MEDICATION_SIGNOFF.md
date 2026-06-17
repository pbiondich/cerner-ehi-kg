# SA_MEDICATION_SIGNOFF

> Contains records that document the amount of medication that was wasted and returned Based on the number of medications they use that are controlled medications. Estimate it's a 1:3 with SA_MEDICATION. 87,000

**Description:** SA Medication Signoff  
**Table type:** ACTIVITY  
**Primary key:** `SA_MEDICATION_SIGNOFF_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PREVIOUS_MED_SIGNOFF_ID` | DOUBLE | NOT NULL | FK→ | The id to the signoff record before the record was changed. If 0, this is the original unchanged record |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who is signing the amounts returned and wasted |
| 7 | `RETURNED_QTY` | DOUBLE |  |  | The amount of the medication that was returned |
| 8 | `SA_MEDICATION_ID` | DOUBLE | NOT NULL | FK→ | The SA_MEDICATION record id that this administration record is documenting |
| 9 | `SA_MEDICATION_SIGNOFF_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the medication signoff record |
| 10 | `SIGNED_DT_TM` | DATETIME |  |  | The date/time the user signed off on the amount returned and wasted |
| 11 | `SIGNED_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates what type of signature this record is for, 1=signed, 2=witnessed |
| 12 | `TOTAL_DISPENSED_QTY` | DOUBLE | NOT NULL |  | Total amout of Dispensed Quantity |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Volume code |
| 19 | `WASTED_QTY` | DOUBLE |  |  | The amount of the medication that was wasted |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREVIOUS_MED_SIGNOFF_ID` | [SA_MEDICATION_SIGNOFF](SA_MEDICATION_SIGNOFF.md) | `SA_MEDICATION_SIGNOFF_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_MEDICATION_ID` | [SA_MEDICATION](SA_MEDICATION.md) | `SA_MEDICATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_MEDICATION_SIGNOFF](SA_MEDICATION_SIGNOFF.md) | `PREVIOUS_MED_SIGNOFF_ID` |
| [SA_MED_SIGNOFF_SIGNATURE](SA_MED_SIGNOFF_SIGNATURE.md) | `SA_MEDICATION_SIGNOFF_ID` |

