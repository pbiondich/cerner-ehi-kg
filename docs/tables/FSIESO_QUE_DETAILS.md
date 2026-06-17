# FSIESO_QUE_DETAILS

> This table holds referential identifiers for events in the CQM_FSIESO_QUE table.

**Description:** CQM_FSIESO_QUE table details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ATTRIBUTE_TXT` | VARCHAR(100) |  |  | The value of the Parent Entity when the associated Parent Entity ID is a String value or the Parent Entity is a Column and the column value is alphanumeric. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the phone row is related (i.e., person_id, organization_id, etc.) |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this phone row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 4 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CQM queue table. It is an internal system assigned number. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUEUE_ID` | [CQM_FSIESO_QUE](CQM_FSIESO_QUE.md) | `QUEUE_ID` |

