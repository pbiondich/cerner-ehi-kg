# PRSNL_LOC_TEMPLATE_RELTN

> allows for associating textual templates (defined on CLINICAL_NOTE_TEMPLATE) to specific facilities to allow for more focused lists of templates based on the current encounter being used when documenting a note for a patient (in Clinical Notes / PowerNote).

**Description:** Personnel, Location, and Template Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE |  |  | An indicator that signifies whether this template is the default template for the location or person. |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location (facility) to which the template is associated. |
| 3 | `NOTE_TYPE_TEMPLATE_RELTN_ID` | DOUBLE | NOT NULL | FK→ | The template to note type relationship identifier from the note_type_template_reltn table. |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person to which the template is associated. |
| 5 | `PRSNL_LOC_TEMPLATE_RELTN_ID` | DOUBLE | NOT NULL |  | A unique identifier for a relationship between a personnel and a template or a location and a template. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTE_TYPE_TEMPLATE_RELTN_ID` | [NOTE_TYPE_TEMPLATE_RELTN](NOTE_TYPE_TEMPLATE_RELTN.md) | `NOTE_TYPE_TEMPLATE_RELTN_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

