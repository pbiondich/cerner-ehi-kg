# PREGNANCY_CHILD

> This table stores the data relating to a particular child of a pregnancy

**Description:** Pregnancy Child  
**Table type:** ACTIVITY  
**Primary key:** `PREGNANCY_CHILD_ID`  
**Columns:** 33  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANESTHESIA_TXT` | VARCHAR(60) |  |  | Free text description of type of anesthesia used during delivery procedure |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CHILD_COMMENT_ID` | DOUBLE | NOT NULL |  | LONG_TEXT id for a comment related to the child |
| 5 | `CHILD_NAME` | VARCHAR(60) |  |  | Name of the child |
| 6 | `DELIVERY_DATE_PRECISION_FLAG` | DOUBLE | NOT NULL |  | Indicates the level of precision known for the delivery date (day, week, month, year) 0 = day; 1 = month; 2 = year |
| 7 | `DELIVERY_DATE_QUALIFIER_FLAG` | DOUBLE | NOT NULL |  | Provides additional detail for imprecise delivery dates (about, after, before)0 = no qualifier; 1 = before; 2 = about; 3 = after; 4 = Date Only - Time should not be used. |
| 8 | `DELIVERY_DT_TM` | DATETIME |  |  | Date/time at which the child was delivered |
| 9 | `DELIVERY_HOSPITAL` | VARCHAR(60) |  |  | Location in which the child was delivered |
| 10 | `DELIVERY_METHOD_CD` | DOUBLE | NOT NULL |  | Method by which the child was delivered |
| 11 | `DELIVERY_PROVIDER_NAME` | VARCHAR(60) |  |  | Name of provider/physician who has performed this delivery. |
| 12 | `DELIVERY_TZ` | DOUBLE | NOT NULL |  | Time zone in which the child was delivered |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FATHER_NAME` | VARCHAR(60) |  |  | Name of child's father |
| 15 | `GENDER_CD` | DOUBLE | NOT NULL |  | Gender of the child |
| 16 | `GESTATION_AGE` | DOUBLE | NOT NULL |  | Child's gestational age, in days, on date of delivery |
| 17 | `GESTATION_TERM_TXT` | VARCHAR(20) |  |  | Child's gestational age when user is not sure of exact gestation weeks and days |
| 18 | `LABOR_DURATION` | DOUBLE | NOT NULL |  | Duration in minutes of thelabor for the delivery of the child. |
| 19 | `NEONATE_OUTCOME_CD` | DOUBLE | NOT NULL |  | Indicates the outcome of the pregnancy for the child |
| 20 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the child on the PERSON table, if a corresponding record exists |
| 21 | `PREGNANCY_CHILD_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 22 | `PREGNANCY_ID` | DOUBLE | NOT NULL | FK→ | PREGNANCY INSTANCE ID |
| 23 | `PREGNANCY_INSTANCE_ID` | DOUBLE | NOT NULL | FK→ | The PREGNANCY_INSTANCE_ID value from the PREGNANCY_INSTANCE table that this action corresponds to. |
| 24 | `PRETERM_LABOR_TXT` | VARCHAR(255) | NOT NULL |  | Free text description of preterm labor occurring during the pregnancy |
| 25 | `RESTRICT_PERSON_ID_IND` | DOUBLE | NOT NULL |  | A value of 1 indicates that the relationship between the person_id and this pregnancy has been made restricted and should not be used to correlate data from that chart with the pregnancy. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `VBAC_IND` | DOUBLE |  |  | Indicates whether this delivery is vaginal birth after cesarean (VBAC) or not. Value 1 indicates it is vbac and 0 indicates it is not vbac. |
| 32 | `WEIGHT_AMT` | DOUBLE |  |  | Birth weight |
| 33 | `WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measurement for birth weight |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PREGNANCY_ID` | [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PREGNANCY_INSTANCE_ID` |
| `PREGNANCY_INSTANCE_ID` | [PREGNANCY_INSTANCE](PREGNANCY_INSTANCE.md) | `PREGNANCY_INSTANCE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PREGNANCY_CHILD_ENTITY_R](PREGNANCY_CHILD_ENTITY_R.md) | `PREGNANCY_CHILD_ID` |

