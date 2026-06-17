# MP_VIEWPOINT_RELTN

> Stores the components that are a part of the MPages Viewpoint. Shows the relationship between a viewpoint and the views that are associated with the viewpoint (For Viewpoint X; Ambulatory Summary, Inpatient Summary, ICU Summary and a View Builder page are associated)

**Description:** MPages Viewpoint Relation  
**Table type:** REFERENCE  
**Primary key:** `MP_VIEWPOINT_RELTN_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | The Bedrock category that is related to this Viewpoint. |
| 2 | `MP_VIEWPOINT_ID` | DOUBLE | NOT NULL | FK→ | The MPages Viewpoint that is associated with this Bedrock Category. |
| 3 | `MP_VIEWPOINT_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the MP_VIEWPOINT_RELTN table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VIEW_SEQ` | DOUBLE | NOT NULL |  | Sequences the tabs within a view. The tab is a Bedrock category. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_CATEGORY_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |
| `MP_VIEWPOINT_ID` | [MP_VIEWPOINT](MP_VIEWPOINT.md) | `MP_VIEWPOINT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MP_VIEWPOINT_ENCNTR](MP_VIEWPOINT_ENCNTR.md) | `MP_VIEWPOINT_RELTN_ID` |

