# OMF_AUDIT_CAT

> Categories of logical parameters associated with audit events.

**Description:** OMF Audit Category  
**Table type:** REFERENCE  
**Primary key:** `AUDIT_CAT_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_CAT_CD` | DOUBLE | NOT NULL |  | That categories that are eligible to be audited. |
| 2 | `AUDIT_CAT_ID` | DOUBLE | NOT NULL | PK | Unique, generated key for the OMF_AUDIT_CAT table. |
| 3 | `AUDIT_EVENT_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to the AUDIT_EVENT table. This is the audit event/audit type pairing associated with this audit category. |
| 4 | `PARTICIPANT_ID_TYPE_TXT` | VARCHAR(100) | NOT NULL |  | The specific type of information that is audited. For example: person_id, Account Number |
| 5 | `PARTICIPANT_ROLE_TXT` | VARCHAR(100) | NOT NULL |  | The functional application role of Participant. The general category of the object being audited. For example, Patient, Provider. |
| 6 | `PARTICIPANT_TYPE_TXT` | VARCHAR(100) | NOT NULL |  | The general category of data that is to be audited. For example, Person, Organization |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUDIT_EVENT_NBR` | [AUDIT_EVENT](AUDIT_EVENT.md) | `AUDIT_EVENT_NBR` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OMF_AUDIT_CAT_GRID_RELTN](OMF_AUDIT_CAT_GRID_RELTN.md) | `AUDIT_CAT_ID` |
| [OMF_AUDIT_CAT_IND_RELTN](OMF_AUDIT_CAT_IND_RELTN.md) | `AUDIT_CAT_ID` |

