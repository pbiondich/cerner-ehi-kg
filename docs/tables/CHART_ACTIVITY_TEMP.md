# CHART_ACTIVITY_TEMP

> This table is temporary and will store the event codes and catalog codes associated to the distribution format. This table was created to utilize direct Oracle joins instead of using dummyt tables when combining against the event_cds and catalog_cds for a given format.

**Description:** Chart Activity Temp  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Orderable. From code set 200 |
| 2 | `CONTENT_TYPE_MEAN` | VARCHAR(12) |  |  | stores content type cdf meaning for corresponding rows when used. |
| 3 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier representing the distribution being processed. |
| 4 | `EVENT_CD` | DOUBLE | NOT NULL |  | The Event Code from code set 72 |
| 5 | `FLEX_TYPE_FLAG` | DOUBLE | NOT NULL |  | Used for Blood Bank and HLA chart sections to determine what type sections were selected. Blood Bank can be Transfusion or Crossmatch. HLA can have a Typing or Haplotype section. |
| 6 | `PROCEDURE_TYPE_FLAG` | DOUBLE | NOT NULL |  | A value of 0 implies that an event set was assigned to the format while 1 implies orderables were assigned. |
| 7 | `SECT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Represents the type of section such as AP, Gen Lab, PowerForms, etc. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTION_ID` | [CHART_DISTRIBUTION](CHART_DISTRIBUTION.md) | `DISTRIBUTION_ID` |

