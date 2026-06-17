# SCH_CLINIC_RELTN

> Relationship between Clinics and other scheduling data such as medical services, templates, resources.

**Description:** SCHEDULING CLINIC RELATIONSHIPS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `ORIG_SCH_CLINIC_RELTN_ID` | DOUBLE | NOT NULL |  | Contains the PK value of the Original (Effective) Row for this versioned group. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key from the table contained in the parent_entity_name field. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The parent table for the ID contained in the parent_entity_id field |
| 7 | `SCH_CLINIC_ID` | DOUBLE | NOT NULL | FK→ | FK VALUE FROM THE SCH_CLINIC TABLE |
| 8 | `SCH_CLINIC_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCH_CLINIC_ID` | [SCH_CLINIC](SCH_CLINIC.md) | `SCH_CLINIC_ID` |

