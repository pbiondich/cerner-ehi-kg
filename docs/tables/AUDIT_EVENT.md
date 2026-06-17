# AUDIT_EVENT

> The definitions of all possible audit events. Also indicates which events are being actively audited.

**Description:** Audit event definition  
**Table type:** REFERENCE  
**Primary key:** `AUDIT_EVENT_NBR`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDED_DT_TM` | DATETIME |  |  | The date the audit event was added.. |
| 2 | `AUDIT_EVENT_NBR` | DOUBLE | NOT NULL | PK | This is the primary key to the table. It is used in implementation and should not be exposed outside of the audit management system. |
| 3 | `AUDIT_IND` | DOUBLE | NOT NULL |  | Indicates whether the audit event is being actively audited. This field can be modified on the client site. Allowed values are 0 (not auditable) and 1 (auditable). The default value for all audit events is 0 (not auditable). |
| 4 | `AUDIT_NAME_DEF_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to the audit_name_def table. This indicates which audit name definition is being used for the audit event record. |
| 5 | `AUDIT_TYPE_DEF_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to the audit_type_def table. This indicates which audit type definition is being used for the audit event record. |
| 6 | `COMPONENT_NAME` | VARCHAR(125) | NOT NULL |  | The component that utilizes this audit event. |
| 7 | `DESCRIPTION_TEXT` | VARCHAR(2000) |  |  | Description of the audit event. |
| 8 | `EVENT_STATE_CD` | DOUBLE | NOT NULL |  | The state of the audit event. Examples include valid, recommended, best practice, obsolete, etc. |
| 9 | `SOLUTION_FAMILY_NAME` | VARCHAR(125) | NOT NULL |  | The family of solutions this event belongs to. |
| 10 | `SOLUTION_NAME` | VARCHAR(128) |  |  | The name of the solution with which the audit event is applicable. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUDIT_NAME_DEF_NBR` | [AUDIT_NAME_DEF](AUDIT_NAME_DEF.md) | `AUDIT_NAME_DEF_NBR` |
| `AUDIT_TYPE_DEF_NBR` | [AUDIT_TYPE_DEF](AUDIT_TYPE_DEF.md) | `AUDIT_TYPE_DEF_NBR` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AUDIT_REQUEST](AUDIT_REQUEST.md) | `AUDIT_EVENT_NBR` |
| [OMF_AUDIT_CAT](OMF_AUDIT_CAT.md) | `AUDIT_EVENT_NBR` |

