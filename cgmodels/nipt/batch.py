from pydantic import BaseModel


class NiptData(BaseModel):
    result_file: str
    multiqc_report: str
    segmental_calls: List[str]
    
