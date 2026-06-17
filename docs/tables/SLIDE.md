# SLIDE

> This activity table includes records for slides that are created from specimens or blocks. Parameters associated with the slide, such as the stain, slide count category (half-slide, full-slide), and slide origin (specimen or block) are stored.

**Description:** Slide  
**Table type:** ACTIVITY  
**Primary key:** `SLIDE_ID`  
**Columns:** 25  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CASE_SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case and specimen information stored on the CASE_SPECIMEN activity table. This field is filled out only when the slide inventory is created from a specimen. |
| 2 | `CASSETTE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to cassette information stored on the CASSETTE activity table. This field is filled out only when the slide inventory is created from a cassette. |
| 3 | `DISCARD_DT_TM` | DATETIME |  |  | The date and time the slide was disposed. |
| 4 | `DISCARD_REASON_CD` | DOUBLE | NOT NULL |  | The reason why the slide was disposed. |
| 5 | `LABEL_CREATE_DT_TM` | DATETIME |  |  | The date and time the last label was created. |
| 6 | `LABEL_CREATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of method used to creat the label.0 = Spooled,1 = Flat File3 = Nice Label Flat File |
| 7 | `ON_LOAN_LOCN_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 8 | `ORIGINAL_STORAGE_DT_TM` | DATETIME |  |  | The date and time the slide was placed in storage. |
| 9 | `ORIGIN_MODIFIER` | CHAR(7) |  |  | If a slide modifier value was associated with the processing task that caused the row to be added to the SLIDE table, the modifier value entered by the user is stored in this field. |
| 10 | `OWNER_ID` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 11 | `SCREENING_IND` | DOUBLE | NOT NULL |  | Indicated screening status of the slide. |
| 12 | `SEQUENCE_NBR` | DOUBLE |  |  | This field contains a sequence value used to identify the relationship from one slide to the next for a single case. |
| 13 | `SLIDE_CREATE_METHOD_FLAG` | DOUBLE | NOT NULL |  | Slides can be created manually or automatically. Individually created slides could have been created as part of a group ordered by a user or by themselves one at a time by the user. A slide created automatically can occur when a user orders a stain which requires an unstained slide to apply the stain to and the unstained slide does not exist to do so. |
| 14 | `SLIDE_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a row (a slide) included in the SLIDE table. |
| 15 | `SPECIAL_STAIN_IND` | DOUBLE |  |  | If the slide was designated as a stained slide, this field stores the internal identification code associated with the discrete task associated with the specific stain. This value could be used to join to the discrete task assay tables. |
| 16 | `STAIN_TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the processing task representing the activity which, through its completion, caused the slide to be stained. This code could be used to join to the discrete_task_assay table. |
| 17 | `STORAGE_LOCATION_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 18 | `SUPPLEMENTAL_TAG` | CHAR(2) |  |  | This field is not used at this time. |
| 19 | `TAG_ID` | DOUBLE | NOT NULL | FK→ | This field stores the reference to the actual identification code value associated with the slide. The identification code values are stored on the AP_TAG_GROUP and AP_TAG reference tables. |
| 20 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field stores the internal identification code associated with the discrete task that caused the row to be added to the SLIDE table. This value could be used to join to the discrete task assay tables. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_SPECIMEN_ID` | [CASE_SPECIMEN](CASE_SPECIMEN.md) | `CASE_SPECIMEN_ID` |
| `CASSETTE_ID` | [CASSETTE](CASSETTE.md) | `CASSETTE_ID` |
| `STAIN_TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `TAG_ID` | [AP_TAG](AP_TAG.md) | `TAG_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_DIGITAL_SLIDE](AP_DIGITAL_SLIDE.md) | `SLIDE_ID` |
| [PROCESSING_TASK](PROCESSING_TASK.md) | `SLIDE_ID` |

