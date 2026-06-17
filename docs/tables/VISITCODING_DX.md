# VISITCODING_DX

> The subtable for audit trail serving as a pointer to the list of diagnosises that were selected during professional coding.

**Description:** Coding Audit Bill Items Diagnosis  
**Table type:** ACTIVITY  
**Primary key:** `VISITCODING_DX_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Diagnosis |
| 2 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | THE FOREIGN KEY VALUE FROM NOMENCLATURE TABLE |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `VISITCODING_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to tracking_audit |
| 9 | `VISITCODING_DX_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAGNOSIS_ID` | [DIAGNOSIS](DIAGNOSIS.md) | `DIAGNOSIS_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `VISITCODING_AUDIT_ID` | [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `VISITCODING_AUDIT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [VISITCODING_BILLITEM](VISITCODING_BILLITEM.md) | `VISITCODING_DX_ID` |

