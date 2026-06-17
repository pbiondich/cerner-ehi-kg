# ORDER_RECON

> Stores information related to a specific order reconciliation conversation.

**Description:** Order Reconciliation  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_RECON_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CROSS_ENCNTR_IND` | DOUBLE | NOT NULL |  | The table row was created by a reconciliation intended to bridge care from one encounter to another. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The ID of the encounter this order reconciliation is related to. |
| 3 | `NEXT_LOC_CD` | DOUBLE | NOT NULL |  | The next level of care code of where the patient will be admitted, transferred or discharged to after this reconciliation. |
| 4 | `NO_KNOWN_MEDS_IND` | DOUBLE | NOT NULL |  | Indicates if medications existed during the reconciliation conversation. 0 - Meds were reconciled. 1 - No meds were reconciled. |
| 5 | `ORDER_RECON_ID` | DOUBLE | NOT NULL | PK | The primary identifier of this table. |
| 6 | `PERFORMED_DT_TM` | DATETIME | NOT NULL |  | The date and time that the reconciliation took place. |
| 7 | `PERFORMED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel identifier of the user that performed the reconciliation. |
| 8 | `PERFORMED_TZ` | DOUBLE | NOT NULL |  | Performed personnel time zone at the time of reconciliation. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person ID from the person table on which this reconciliation was performed. |
| 10 | `RECON_STATUS_CD` | DOUBLE | NOT NULL |  | The reconciliation status code. Field can be 0.0 or a value from code set 4002695. |
| 11 | `RECON_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of reconciliation that was performed. 1 - Admission, 2 - Transfer, 3 - Discharge, 4 - Short Term Leave, 5 - Return From Short Term Leave |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERFORMED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ORDER_RECON_DETAIL](ORDER_RECON_DETAIL.md) | `ORDER_RECON_ID` |

