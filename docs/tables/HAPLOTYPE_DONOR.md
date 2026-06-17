# HAPLOTYPE_DONOR

> Records the potential donors related to the potential recipient's haplotype chart, the haplotype of each of these donors and comments about each of these donors.

**Description:** Haplotype Donor  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where comments for a haplotype chart donor are stored. It is a foreign key reference to the primary key of the long_text table. |
| 2 | `CREATED_DT_TM` | DATETIME |  |  | The date and time this donor was added to the haplotype chart. |
| 3 | `HAPLOTYPE` | VARCHAR(255) |  |  | Text string representing the Antigens which make up the first of a donor's two haplotypes. |
| 4 | `HAPLOTYPE2` | VARCHAR(255) |  |  | Text string representing the Antigens which make up the second of a donor's two haplotypes. |
| 5 | `HAPLOTYPE2_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | Identifier for the second of a donor's haplotypes. Used as an alias to the haplotype to more easily denote that persons have identical haplotypes. |
| 6 | `HAPLOTYPE_ASSIGNMENT_CD` | DOUBLE | NOT NULL |  | Identifier for the first of a donor's haplotypes. Used as an alias to the haplotype to more easily denote that persons have identical haplotypes. |
| 7 | `HAPLOTYPE_CHART_ID` | DOUBLE | NOT NULL | FK→ | Relates this haplotype donor to a haplotype chart for a specific potential recipient. It is a foreign key reference to the primary key of the Haplotype Chart table. |
| 8 | `HAPLOTYPE_DONOR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the haplotype_donor table. It is an internal system assigned number. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `REMOVED_DT_TM` | DATETIME |  |  | The date and time this donor was removed from the haplotype chart. Haplotype_donor record are not deleted so that an audit trail can be kept. |
| 11 | `REMOVED_IND` | DOUBLE |  |  | Indicates that this donor was removed from the haplotype chart. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `HAPLOTYPE_CHART_ID` | [HAPLOTYPE_CHART](HAPLOTYPE_CHART.md) | `HAPLOTYPE_CHART_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

