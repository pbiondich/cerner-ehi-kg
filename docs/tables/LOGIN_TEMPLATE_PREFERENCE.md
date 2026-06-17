# LOGIN_TEMPLATE_PREFERENCE

> Stores the detail preferences of each login template. Login Templates control the behavior of the PathNet Collections: Specimen Login application

**Description:** Login Template Preference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PREFERENCE` | DOUBLE | NOT NULL |  | This field defines a particular preference for a login type (see template_type field) on a login template (see template_cd field). Preferences include which spreadsheet columns are visible; sort order for spreadsheet column headings; default values for collected and received date, time, and id; etc. |
| 2 | `TEMPLATE_CD` | DOUBLE | NOT NULL | FK→ | The code value identifying a particular login template. |
| 3 | `TEMPLATE_TYPE` | DOUBLE | NOT NULL |  | This field identifies with which type of log-in this row's preference is associated. Possible values include 0 (general -- more general options such as which log-in types are enabled on this template), 1 (log-in by user), 2 (log-in by location), 3 (log-in by list), 4 (log-in by patient), 5 (log-in by accession). All 5 log-in types are defined for each template. This field is used to further subclass them so they can be pulled back individually. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALUE` | DOUBLE |  |  | This field defines the actual value for a log-in template preference. In other words, it is this field that defines what options are turned on and off on a given log-in template. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TEMPLATE_CD` | [LOGIN_TEMPLATE](LOGIN_TEMPLATE.md) | `TEMPLATE_CD` |

