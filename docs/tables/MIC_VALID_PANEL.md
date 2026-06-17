# MIC_VALID_PANEL

> This table associates the antibiotic and ID panels with the procedure/service resource/source and organism combination defined on the mic_valid_sus_panel table.

**Description:** Microbiology Valid Panels  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_PANEL_IND` | DOUBLE |  |  | This field indicates if the selected valid panel should be defined as a default panel and automatically display in result entry when the susceptibility method is ordered. Valid values include: 0 = Not a default panel 1 = Default panel |
| 2 | `ID_ONLY_IND` | DOUBLE |  |  | This field indicates if the selected panel is a detail automated ID biochemical. Valid values include: 0 = Not an automated ID biochemical. 1 = Automated ID biochemical. |
| 3 | `PANEL_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the antibiotic panel defined as valid for the valid_panel_id. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VALID_PANEL_ID` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each set of valid susceptibility panels defined for an orderable procedure/service resource/source and organism combination. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VALID_PANEL_ID` | [MIC_VALID_SUS_PANEL](MIC_VALID_SUS_PANEL.md) | `VALID_PANEL_ID` |

