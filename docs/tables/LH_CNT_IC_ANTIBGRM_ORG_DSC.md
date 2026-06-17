# LH_CNT_IC_ANTIBGRM_ORG_DSC

> Holds the Disclaimer or Suppress information for Antibiogram Reporting

**Description:** LH_CNT_IC_ANTIBGRM_ORG_DSC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | antibiotic for this grouping |
| 2 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Facility for this grouping |
| 3 | `LH_CNT_IC_ANTIBGRM_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Related row on LH_CNT_IC_BR_GROUP table |
| 4 | `LH_CNT_IC_ANTIBGRM_ORG_DSC_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_ANTIBGRM_ORG_DSC table. |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | disclaimer text |
| 6 | `ORGANISM_CD` | DOUBLE | NOT NULL |  | organism for this grouping |
| 7 | `SUPPRESS_IND` | DOUBLE | NOT NULL |  | suppress indicator if = 1 then this grouping will not display in reporting |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_ANTIBGRM_GROUP_ID` | [LH_CNT_IC_ANTIBGRM_GROUP](LH_CNT_IC_ANTIBGRM_GROUP.md) | `LH_CNT_IC_ANTIBGRM_GROUP_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

