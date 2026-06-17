# SN_CHARGE_HEADER

> SurgiNet Charge Header Table

**Description:** SurgiNet Charge Header  
**Table type:** ACTIVITY  
**Primary key:** `CHARGE_HEADER_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANESTH_TYPE_CD` | DOUBLE | NOT NULL |  | The primary anesthesia type associated with the surgical case. |
| 2 | `CASE_LEVEL_CD` | DOUBLE | NOT NULL |  | The case level associated with the surgical case. |
| 3 | `CHARGE_HEADER_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a charge header. |
| 4 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type associated with the surgical case. |
| 5 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | Surgical cases need to be able to have their charges flexed by the priority of a case. If a case is an emergency case that is not planned for the charges will probably be higher due to the costs associated with shuffling all other work around and potentially bringing in additional staff to accommodate the case. |
| 6 | `SERVICE_DT_TM` | DATETIME |  |  | The date and time of either the start of the surgery or the patient in- room. |
| 7 | `SURGEON_PRSNL_ID` | DOUBLE | NOT NULL |  | The primary surgeon associated with this charge header. |
| 8 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | The surgical case associated with this charge header. |
| 9 | `SURG_OP_LOC_CD` | DOUBLE | NOT NULL |  | The OR number associated with the surgical case. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_CHARGE_DETAIL](SN_CHARGE_DETAIL.md) | `CHARGE_HEADER_ID` |

