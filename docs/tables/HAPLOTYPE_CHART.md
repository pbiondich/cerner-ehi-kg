# HAPLOTYPE_CHART

> Records the haplotype of the potential recipient and comments about the haplotype chart as a whole.

**Description:** Haplotype Chart  
**Table type:** ACTIVITY  
**Primary key:** `HAPLOTYPE_CHART_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where haplotype chart comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 6 | `HAPLOTYPE` | VARCHAR(255) |  |  | Text string representing the Antigens which make up the first of a recipient's two haplotypes. |
| 7 | `HAPLOTYPE2` | VARCHAR(255) |  |  | Text string representing the Antigens which make up the second of a recipient's two haplotypes. |
| 8 | `HAPLOTYPE2_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | Identifier for the second of a recipient's haplotypes. Used as an alias to the haplotype to more easily denote that persons have identical haplotypes. |
| 9 | `HAPLOTYPE_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | Identifier for the first of a recipient's haplotypes. Used as an alias to the haplotype to more easily denote that persons have identical haplotypes. |
| 10 | `HAPLOTYPE_CHART_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the haplotype_chart table. It is an internal system assigned number. |
| 11 | `MATERNAL_DEDUCED_IND` | DOUBLE |  |  | No longer used. |
| 12 | `PARENTAL_IND` | DOUBLE |  |  | No longer used. |
| 13 | `PATERNAL_DEDUCED_IND` | DOUBLE |  |  | No longer used. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HAPLOTYPE_DONOR](HAPLOTYPE_DONOR.md) | `HAPLOTYPE_CHART_ID` |
| [PHENOTYPE_LOCI](PHENOTYPE_LOCI.md) | `HAPLOTYPE_CHART_ID` |

